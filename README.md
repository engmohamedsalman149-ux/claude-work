# Claude ↔ After Effects: تحكم كامل

المشروع ده بيخلّي Claude يتحكم في **Adobe After Effects** بالكامل: يعمل كومبوزيشنز ولايرز ونصوص وشيبس، ويحرّك بالكي فريمز والإيزنج، ويحط إكسبريشنز وإفكتات، ويستورد ملفات، ويرندر، ويشوف الفريم اللي طلع علشان يراجع شغله. ولو فيه حاجة مش موجودة كأداة جاهزة، يقدر يكتب ويشغّل أي ExtendScript جوه After Effects.

```
Claude (Desktop / Code)  ──MCP──►  mcp-server (Node.js)  ──ملفات JSON──►  ClaudeBridge.jsx (بانل جوه After Effects)
```

- `after-effects/ClaudeBridge.jsx`: بانل جوه After Effects. بيقرا الأوامر من فولدر مشترك وينفذ كل أمر في Undo Group لوحده، يعني تقدر تعمل Ctrl+Z لأي حاجة Claude عملها.
- `mcp-server/`: سيرفر MCP بيعرض الأدوات لـ Claude.

## التسطيب

### 1) جوه After Effects

1. انسخ `after-effects/ClaudeBridge.jsx` في فولدر **ScriptUI Panels**:
   - Windows: `C:\Program Files\Adobe\Adobe After Effects <الإصدار>\Support Files\Scripts\ScriptUI Panels\`
   - macOS: `/Applications/Adobe After Effects <الإصدار>/Scripts/ScriptUI Panels/`
2. من **Edit › Preferences › Scripting & Expressions** (على الماك: **After Effects › Settings**) فعّل
   **Allow Scripts to Write Files and Access Network**.
3. اقفل After Effects وافتحه تاني، وبعدين افتح **Window › ClaudeBridge.jsx**. البانل بيبدأ لوحده ويكتب `Listening on ...`.
   سيب البانل مفتوح (ممكن تعمله Dock في أي مكان).

### 2) سيرفر MCP

محتاج Node.js 18 أو أحدث:

```bash
cd mcp-server
npm install
```

**Claude Desktop**: ضيف ده لملف `claude_desktop_config.json` (من Settings › Developer › Edit Config):

```json
{
  "mcpServers": {
    "after-effects": {
      "command": "node",
      "args": ["C:/path/to/claude-work/mcp-server/src/index.js"]
    }
  }
}
```

**Claude Code**:

```bash
claude mcp add after-effects -- node /path/to/claude-work/mcp-server/src/index.js
```

بعدها اسأل Claude: «شوف After Effects متوصل؟» وهو هيستخدم `ae_status`.

> لازم Claude والسيرفر و After Effects يكونوا على **نفس الجهاز**. جلسة Claude Code في الكلاود مش هتقدر توصل لـ After Effects اللي على جهازك.

## الأدوات المتاحة

| الأداة | بتعمل إيه |
|---|---|
| `ae_status` | تتأكد إن After Effects متوصل |
| `ae_run_script` | تشغّل أي ExtendScript وترجّع النتيجة (تحكم كامل في الـ API) |
| `ae_project_info`, `ae_list_items`, `ae_project_file` | معلومات المشروع، عناصر البروجكت، حفظ/فتح/جديد/قفل |
| `ae_import_file` | استيراد فيديو/صور/صوت/PSD/AI/Image sequence |
| `ae_get_comp`, `ae_create_comp`, `ae_set_comp`, `ae_precompose` | إدارة الكومبوزيشنز |
| `ae_add_layer` | Solid, Text, Shape, Null, Camera, Light, Adjustment أو أي Item من البروجكت |
| `ae_add_shape` | مستطيل، دايرة، نجمة، مضلع أو Path مع Fill و Stroke |
| `ae_modify_layer`, `ae_layer_action` | إعدادات اللاير، Parent، 3D، Blending، Track Matte، مسح/تكرار/ترتيب/Split |
| `ae_layer_properties`, `ae_get_property`, `ae_set_property` | قراءة وتعديل أي Property (Transform، إفكتات، نص، ألوان الشيب...) |
| `ae_set_keyframes` | أنيميشن بالكي فريمز مع Easy Ease و Linear و Hold |
| `ae_set_expression` | إكسبريشنز، وبيرجع أي Error |
| `ae_add_effect`, `ae_list_effects` | إضافة أي إفكت متسطب وضبط قيمه |
| `ae_menu_command` | تشغيل أي أمر من القوايم (Undo, Redo...) |
| `ae_render` | رندر من الـ Render Queue أو إرسال لـ Media Encoder |
| `ae_preview_frame` | يرندر فريم ويرجّعه صورة علشان Claude يشوف النتيجة |

مسارات الـ Properties بتقبل الأسماء أو الـ match names، زي `Transform/Position` أو `Effects/Gaussian Blur/Blurriness` أو `Text/Source Text`. الأسماء الأساسية (Transform, Position, Scale, Opacity, Effects, Text...) بتشتغل حتى لو واجهة After Effects بلغة تانية.

## تحليل حركات المونتاج وحفظها بأسماء

الأداة دي بتحلل أي فيديو وتطلع حركات المونتاج اللي فيه، وبعدين تحفظ كل حركة باسم تختاره، علشان لما تقول «نفّذ الانتقال ده على الفيديو ده» Claude يعمله في After Effects بنفس التوقيت والشكل.

**1. التحليل:** `video_analyze` بيستخدم ffmpeg (بيتسطب لوحده مع `npm install`) ويطلع:
- القطعات (Hard cut)، الـ Dissolve، الـ Dip to black، الفلاش الأبيض، والانتقالات اللي فيها حركة سريعة (Zoom / Whip / Spin / Glitch).
- إيقاع المونتاج: طول كل لقطة، عدد القطعات في الدقيقة، وهل القطعات ماشية على البيت (من الصوت).
- اللوك (الإضاءة والتباين والتشبع ولون الصورة).
- شريط صور قبل وأثناء وبعد كل حركة، علشان Claude يشوف بعينه ويحدد نوع الحركة بالظبط (مثلاً Zoom in ولا Whip شمال).

**2. الحفظ باسم:** `preset_save` أو `preset_from_event`. تقدر تسمي بالعربي، زي «فلاش أبيض» أو «زووم الإنترو». وممكن كمان تحفظ `look` (لون الفيديو) و `rhythm` (إيقاع القطعات).

**3. التنفيذ:** `preset_apply` على:
- فيديو واحد: بيتحط على كل القطعات اللي فيه تلقائي، أو على ثواني تحددها.
- كذا فيديو: بيرصّهم ورا بعض ويحط الانتقال بين كل اتنين.
- أو كومب ولاير موجودين في After Effects.

كل تطبيق بيبقى Undo واحد.

الحركات اللي المحرك بينفذها: `cut`, `jump_cut`, `crossfade`, `dip`, `flash`, `zoom`, `punch`, `whip`, `spin`, `blur`, `shake`, `push`, `speed_ramp`, `grade`, `effect` (أي إفكت في After Effects بكي فريمز)، و `custom` (سكربت حر لأي حركة مش موجودة). الحركة ممكن تتكون من كذا خطوة مع بعض، زي Zoom + Blur + Flash.

أمثلة:
- «حلل الفيديو `D:/refs/edit.mp4` وقولي فيه حركات إيه.»
- «احفظ الانتقال التالت باسم "زووم فلاش"، واحفظ اللوك باسم "لوك دافي".»
- «نفّذ "زووم فلاش" على `D:/clips/a.mp4` و `D:/clips/b.mp4`.»
- «اعمل الفيديو ده بنفس إيقاع القطعات بتاع الريفرنس وحط "فلاش أبيض" على كل قطع.»
- «طبّق "لوك دافي" على الكومب اللي مفتوح.»

المكتبة بتتحفظ في `claude-edit-library` جنب فولدر البريدج، وتقدر تغيّرها بـ `AE_LIBRARY_DIR`. ولو عايز تستخدم ffmpeg بتاعك، حدد مكانه بـ `FFMPEG_PATH` و `FFPROBE_PATH`.

**حدود التحليل:** التحليل بيعتمد على إشارات الصورة. القطعات والـ Dissolve والـ Dip والفلاش بتتكشف بدقة. أما الانتقالات اللي فيها حركة، فالأداة بتعرف إن فيه انتقال وتوقيته، بس نوعه بيتحدد من الصور. التطبيق بيقرّب الحركة باستخدام أدوات After Effects؛ هو مش نسخة بالبكسل من الأصل.

## أمثلة تقولها لـ Claude

- «اعمل كومب 1080×1920 مدته 15 ثانية، وحط عنوان "أهلاً بيكم" في النص يظهر بـ fade و scale من 80 لـ 100 بـ easy ease.»
- «ضيف لكل اللايرز في الكومب ده Drop Shadow وخلي الـ opacity بتاعه 40.»
- «اعمل Null واربط بيه كل اللايرز، وحط wiggle expression على الـ position.»
- «ورّيني الفريم عند ثانية 3.»
- «رندر الكومب ده لـ `D:/renders/intro.mp4`.»

## ملاحظات

- الأوامر بتتبادل عن طريق فولدر:
  Windows `%APPDATA%\ae-claude-bridge`، macOS `~/Library/Application Support/ae-claude-bridge`.
  تقدر تغيّره من ناحية السيرفر بـ `AE_BRIDGE_DIR`، بس لازم يطابق الفولدر اللي البانل كاتبه.
- **أمان:** أي برنامج يقدر يكتب في الفولدر ده يقدر يشغّل سكربت جوه After Effects. الفولدر جوه البروفايل بتاعك، فمتشغّلش البانل على جهاز مش بتثق فيه.
- لو في Dialog مفتوح في After Effects، الأوامر هتستنى لحد ما تقفله.
- الرندر بيوقف After Effects لحد ما يخلص؛ الـ timeout الافتراضي للرندر 30 دقيقة (غيّره بـ `timeoutSec`).
- النص العربي محتاج إن After Effects يكون شغال بالـ Middle Eastern text engine (من Preferences › Type) علشان الحروف تتوصل صح.
- `ae_preview_frame` بيستخدم `saveFrameToPng`، ودي موجودة في الإصدارات الحديثة من After Effects.

## الاختبارات

```bash
cd mcp-server && npm test
```

الاختبارات بتشغّل السيرفر وبتستبدل After Effects بمحاكي بيرد على الأوامر بنفس بروتوكول البانل.
