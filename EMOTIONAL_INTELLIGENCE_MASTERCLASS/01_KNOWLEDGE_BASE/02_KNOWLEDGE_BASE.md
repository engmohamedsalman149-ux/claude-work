# 02_KNOWLEDGE_BASE — قاعدة المعرفة المتكاملة
**المشروع:** EMOTIONAL INTELLIGENCE — 2-HOUR ARABIC YOUTUBE MASTERCLASS
**المرحلة:** PHASE 2 — KNOWLEDGE EXTRACTION
**المدخلات:** `00_SOURCE_AUDIT/01_SOURCE_AUDIT.md` + `concept_table.csv` (189 صفًا) + ملاحظات القراءة الكاملة في `00_SOURCE_AUDIT/notes/` (GOL · MOM2 · NVC · CC · KZ · FILM).
**المخرج الآلي المصاحب:** `knowledge_base.csv` (نفس المداخل بصيغة جدول — يُولَّد من هذا الملف).

---

## 0. كيف تُقرأ هذه القاعدة

### 0.1 الحقول (كما طلبها الـBrief)
كل مدخل يحتوي على الحقول العشرة: **Concept · Definition · Book · Chapter · Page · Example · Application · Related Concepts · Potential Visual · Potential Exercise** + حقلين إضافيين للضبط:
- **Tag** = نوع الدعم المصدري.
- **CT#** = رقم الصف المقابل في `concept_table.csv` (للتتبع إلى Source Map في المرحلة 11).

### 0.2 الوسوم
| الوسم | المعنى |
|---|---|
| [DIRECT SOURCE] | الفكرة موجودة نصًا في الكتاب المذكور بالصفحة. |
| [REPORTED IN SOURCE] | دراسة/رقم ينقله المؤلف عن غيره — يُقال «بحسب ما ينقله الكتاب». |
| [INTEGRATED SYNTHESIS] | ربط صنعناه بين أكثر من مصدر؛ لا يُنسب لمؤلف واحد. |
| [BOOK DIFFERENCE] | الكتب تختلف — يُعرض الاختلاف ولا يُخفى (D1–D7 في §10). |
| [USER-PROVIDED FRAMEWORK] | من إطار المستخدم في الـBrief (مراحل التعلم، الدرع، النظام النهائي، خطة 7 أيام). |
| [EXTERNAL: WEB] | من بحث ويب موثّق (الفيلم فقط). |
| [EXTERNAL KNOWLEDGE] | معرفة عامة خارج الكتب — تُذكر كذلك صراحة. |
| [NOT SUPPORTED BY PROVIDED SOURCE] | لا يوجد في المصادر المرفقة. |
| [SAFETY] | مادة حساسة: تُستخدم مبادئها فقط، أو تُحال لمتخصص. |

### 0.3 صيغ الإحالة
- **Goleman (GOL):** «الذكاء العاطفي»، ترجمة ليلى الجبالي، عالم المعرفة 262 (2000) — **ص.N** مطبوعة.
- **Mind Over Mood (MoM):** 2nd ed., Guilford 2016 — **p.N** مطبوعة.
- **Nonviolent Communication (NVC):** 3rd ed., PuddleDancer 2015 — **L####** سطر في الملف (لا أرقام صفحات في الملف).
- **Crucial Conversations (CC):** 1st ed., McGraw-Hill 2002 — **p.N** مطبوعة.
- **Wherever You Go, There You Are (KZ):** Hyperion 2004 ebook — **PDF p.N**.
- **FILM:** «الزوجة الثانية» 1967 — `notes/FILM_notes.md` §N.

### 0.4 خريطة الترتيب
المداخل مرتبة حسب **مراحل التعلم الثماني** [USER-PROVIDED FRAMEWORK]، وكل مرحلة مربوطة بقسم Goleman الذي يمثل العمود الفقري:

| المرحلة | الاسم | قسم Goleman المقابل | الكتب المكملة | المداخل |
|---|---|---|---|---|
| 1 | UNDERSTAND — افهم | ق1 المخ الانفعالي + ف3 | MoM (النموذج الخماسي، الإنذار) · CC | KB-001 → KB-017 |
| 2 | NOTICE — لاحظ | ف4 اعرف نفسك | KZ · CC · MoM | KB-018 → KB-034 |
| 3 | NAME + REFRAME — سمِّ وأعد التأطير | ف5 عبيد العاطفة + ف6 | MoM · CC ف6 · NVC ف4–5، 9–10 | KB-035 → KB-057 |
| 4 | EMPATHIZE — تعاطف | ف7 جذور التعاطف + ف8 | NVC ف7–8 · CC ف8 · MoM | KB-058 → KB-071 |
| 5 | COMMUNICATE — تواصل | ف9 الأعداء الحميمون + ف10 | NVC ف1–6، 14 · MoM ف15 | KB-072 → KB-081 |
| 6 | HANDLE CONFLICT — أدِر الخلاف | ف9–10 (التطبيق) | CC · NVC ف11 · MoM ف10 | KB-082 → KB-096 |
| 7 | PROTECT YOURSELF — احمِ نفسك | ف7–8 (الجانب المظلم) + ف12–13 + ف15 | MoM ف3، 9، 12، 15 · NVC ف12 · KZ · CC ف11 · FILM | KB-097 → KB-132 |
| 8 | INTEGRATE — اجمع | ق4 الفرص المتاحة + ق5 محو الأمية العاطفية | MoM ف16 · KZ · CC ف12 | KB-133 → KB-142 |

> **ملاحظة منهجية:** هذا الترتيب [USER-PROVIDED FRAMEWORK] وليس نموذجًا وضعه أي مؤلف. لكن Goleman نفسه يدعم منطق التسلسل في نقطتين: «التعاطف يقوم على أساس الوعي الذاتي» (ص143) و«التعاطف يتطلب قدرًا كافيًا من الهدوء» (ص154–155) ⇒ NOTICE قبل EMPATHIZE، وREGULATE قبل EMPATHIZE.

---

# المرحلة 1 — UNDERSTAND | افهم ما يحدث داخلك
*العمود الفقري: Goleman القسم الأول «المخ الانفعالي» (ف1–2) + ف3 «عندما يخون الذكاء».*

### KB-001 · الذكاء العاطفي | Emotional Intelligence
- **Definition:** مجموعة قدرات: أن تحث نفسك على الاستمرار رغم الإحباط، وتتحكم في النزوات، وتؤجل الإشباع، وتنظّم حالتك النفسية، وتمنع الأسى من شلّ تفكيرك، وتتعاطف وتحتفظ بالأمل (ص54). ويعرضه Goleman عبر نموذج سالوفي في 5 مجالات: معرفة عواطفك، إدارتها، تحفيز النفس، التعرف على عواطف الآخرين، توجيه العلاقات (ص67–68). وهي «عادات… يمكن أن تتحسن».
- **Book:** Goleman
- **Chapter:** مقدمة؛ ف3 «عندما يخون الذكاء»
- **Page:** ص10، ص54، ص67–68
- **Example:** Goleman يفتتح الفصل بطالب متفوق دراسيًا طعن أستاذه بسبب درجة (ص53) ⇒ «الذكاء الأكاديمي ليس له سوى علاقة محدودة بالحياة الانفعالية».
- **Application:** التعريف الافتتاحي للحلقة بعد الـHook — لا يُقدَّم كتعريف أكاديمي بل كإجابة على سؤال «ليه ناس أذكياء بيتصرفوا بغباء وقت الزعل؟».
- **Related Concepts:** KB-002, KB-012, KB-018, KB-058, KB-140
- **Potential Visual:** خماسية سالوفي — 5 دوائر تتصل بمركز «أنت»؛ كل دائرة تضيء في مرحلتها لاحقًا في الحلقة (خيط بصري متكرر).
- **Potential Exercise:** «قيّم نفسك من 1–10 في كل مجال من الخمسة» — تُعاد في نهاية الحلقة للمقارنة.
- **Tag:** [DIRECT SOURCE]
- **CT#:** 1, 150

### KB-002 · تحدي أرسطو | Aristotle's Challenge
- **Definition:** الغضب سهل؛ الصعب أن تغضب «من الشخص المناسب، وبالقدر المناسب، وفي الوقت المناسب، وللهدف المناسب، وبالأسلوب المناسب». Goleman يجعلها سؤال الكتاب: كيف «نسبغ الذكاء على عواطفنا»؟
- **Book:** Goleman (ناقلًا عن أرسطو، «الأخلاق إلى نيقوماخوس»)
- **Chapter:** مقدمة «التحدي الأرسطي»
- **Page:** ص7، ص13
- **Example:** سائق الحافلة في نيويورك الذي تنتقل بهجته للركاب (ص7) — الانفعال يمكن أن يكون قوة إيجابية.
- **Application:** يحدد هدف الحلقة: **ليس إلغاء المشاعر بل إحكامها**. يُستخدم كجملة انتقالية بعد الـHook ومرة أخرى في الختام.
- **Related Concepts:** KB-030, KB-116, KB-001
- **Potential Visual:** 5 أقفال/مفاتيح تُفتح واحدًا تلو الآخر: الشخص — القدر — الوقت — الهدف — الأسلوب.
- **Potential Exercise:** «آخر مرة زعلت: أنهي واحد من الخمسة ضاع منك؟»
- **Tag:** [DIRECT SOURCE] (الاقتباس بترجمة الكتاب العربية)
- **CT#:** 146

### KB-003 · العاطفة نزوع إلى الفعل + بصمة جسدية | Emotion as Impulse to Act
- **Definition:** كلمة emotion أصلها «يتحرك»؛ كل انفعال «نزوع إلى القيام بفعل». لكل انفعال بصمة بيولوجية: الغضب يدفع الدم لليدين والأدرينالين؛ الخوف يدفعه لعضلات الساقين مع تجمد لحظي؛ الحزن يخفض الطاقة؛ الحب يفعّل «الاستجابة المسترخية».
- **Book:** Goleman
- **Chapter:** ف1 «العواطف… لماذا؟»
- **Page:** ص20–22
- **Example:** Goleman يقود في الثلج بكولورادو فيشعر بقلق يدفعه للتوقف، ليكتشف حادثًا أمامه: «الخوف الحذر… ربما أنقذ حياتي» (ص20) — العاطفة مرشد مفيد وليست عدوًا.
- **Application:** يفتتح مرحلة UNDERSTAND: المشاعر «برنامج حركة» قديم، مش عيب فيك.
- **Related Concepts:** KB-004, KB-005, KB-013, KB-024
- **Potential Visual:** «خريطة الجسد العاطفية» — مجسم إنسان تتوهج فيه اليدان (غضب)، الساقان (خوف)، الصدر (حزن)، إلخ.
- **Potential Exercise:** «افتكر آخر مرة اتخضيت: جسمك عمل إيه قبل ما تفكر؟»
- **Tag:** [DIRECT SOURCE]
- **CT#:** 2, 147

### KB-004 · العقلان: عقل يفكر وعقل يشعر | Two Minds
- **Definition:** «في دماغنا عقلان»: عقل منطقي وعقل عاطفي «قوي ومندفع وأحيانًا غير منطقي». العلاقة طردية: كلما اشتدت المشاعر قلّت فاعلية العقل المنطقي. المشاعر ضرورية للتفكير والتفكير مهم للمشاعر، لكن إذا تجاوزت المشاعر «ذروة التوازن» اكتسح العقل العاطفي العقل المنطقي.
- **Book:** Goleman
- **Chapter:** ف1
- **Page:** ص23–28
- **Example:** صديقة بعد طلاقها تقول «لم يعد يهمني حقًا» ثم تغرورق عيناها — الكلمات من عقل، والدموع من عقل آخر (ص23–24).
- **Application:** الأساس المفاهيمي لكل الحلقة: المشكلة ليست «ضعف أخلاق» بل ميزان بين عقلين.
- **Related Concepts:** KB-005, KB-007, KB-010, KB-059
- **Potential Visual:** ميزان أو «مؤشر ضغط» — كلما ارتفعت كفة المشاعر خفتت إضاءة «المفكر».
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]
- **CT#:** 147

### KB-005 · الأميجدالا: فريق الإنذار | Amygdala as Alarm Team
- **Definition:** الأميجدالا (النتوء اللوزي) مركز من مراكز المخ الحوفي، «مخزن للذاكرة العاطفية» وحارس يسأل: «هل أكره هذا؟ هل سيؤذيني؟ هل أخافه؟». تعمل كـ«فريق الإنذار» في البيت: تطلق الطوارئ (اضرب أو اهرب)، تسرّع القلب، تجمّد الوجه، وتستدعي الذكريات المتصلة «قبل استجماع خيوط التفكير».
- **Book:** Goleman
- **Chapter:** ف2 «تشريح النوبات الانفعالية»
- **Page:** ص32–35
- **Example:** الفتاة التي ألقت لوحة ثمينة في القمامة لأن صديقها عنده تمرين، ثم ندمت بعد شهور (ص34) — نوبة صغيرة يومية.
- **Application:** الشخصية الرئيسية في Animation 1–2. تُقدَّم بلغة بسيطة: «جوه دماغك جرس إنذار شغال 24 ساعة».
- **Related Concepts:** KB-006, KB-007, KB-009, KB-014
- **Potential Visual:** غرفة تحكم صغيرة بها جهاز إنذار أحمر (الأميجدالا) وغرفة اجتماعات هادئة (القشرة الأمامية).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] (تبسيط Goleman لعمل LeDoux؛ لا نضيف تفاصيل تشريحية من خارج الكتاب)
- **CT#:** 2

### KB-006 · الطريق المختصر | The Low Road (LeDoux)
- **Definition:** الإشارة من العين/الأذن تذهب إلى المهاد، ومنه **مسار مختصر مباشر** إلى الأميجدالا و**مسار أطول** إلى القشرة الجديدة ⇒ الأميجدالا قد «تبدأ بالاستجابة قبل استجابة القشرة». الاستجابة المختصرة «أسرع (وإن كانت أقل دقة)»: «وسيلة سريعة جدًا… لكنها عملية سريعة كثيرة الأخطاء».
- **Book:** Goleman (عن جوزيف لودو)
- **Chapter:** ف2
- **Page:** ص36–38، ص42–44
- **Example:** Goleman يقفز من سريره الساعة 3 فجرًا ظانًا أن السقف سقط — كانت صناديق زوجته (ص42–43). المضيفة التي أسقطت صينية وجبات عندما رأت سيدة تشبه من تركها زوجها لأجلها (ص44). رقم «12 ملّي ثانية» خاص بالفأر (ص43) — لا يُعمَّم على الإنسان.
- **Application:** Animation 2 «الطريق المختصر vs الطريق الطويل». يشرح لماذا نرد على الرسالة قبل ما نقرأها صح.
- **Related Concepts:** KB-005, KB-007, KB-040
- **Potential Visual:** خريطة طريق: «طريق سريع ترابي» يصل أولًا لكنه يخطئ، و«طريق دائري ممهد» يصل متأخرًا ويرى الصورة كاملة.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE] (أبحاث لودو كما ينقلها Goleman)
- **CT#:** 2

### KB-007 · النوبة الانفعالية | Emotional Hijacking
- **Definition:** لحظة «يعلن فيها المركز الحوفي حالة الطوارئ… قبل أن يتاح للقشرة الجديدة… فرصة لتأمل ما يجري»؛ علامتها أن صاحبها بعدها «لا يعرف ما طرأ عليه»، ويبدو له «بعد قدر من التأمل» أن ما فعله لم يكن له مبرر. تفترض قوتين: قوة تحفز الأميجدالا، وأخرى تُضعف عمل القشرة (ص47). المصطلح في الترجمة: «النوبات الانفعالية/انفلات الأعصاب».
- **Book:** Goleman
- **Chapter:** ف2
- **Page:** ص31، ص47
- **Example:** Goleman يطلب من القارئ: «فكر في آخر مرة فقدت فيها أعصابك… مع زوجتك أو طفلك أو… سائق سيارة» (ص31). CC يصف الشيء نفسه بلغته: «When conversations matter the most… we're generally on our worst behavior» (CC p.4).
- **Application:** قلب الـHook: الرسالة/الموقف ← انفجار ← ندم. تُعطى له تسمية مصرية ثابتة في الحلقة: «لحظة الخطف».
- **Related Concepts:** KB-005, KB-006, KB-008, KB-010, KB-092
- **Potential Visual:** Animation 1 «Emotional Hijack»: عجلة القيادة تنتزعها يد حمراء (الأميجدالا) من يد السائق (القشرة).
- **Potential Exercise:** Exercise 1 (جزء أ): «افتكر آخر لحظة خطف: إيه اللي حصل قبلها بثواني؟»
- **Tag:** [DIRECT SOURCE]; وجه CC = [INTEGRATED SYNTHESIS] (تقاطع لا اقتباس متبادل)
- **CT#:** 2, 4, 5

### KB-008 · مفتاح الإيقاف في الفص الأمامي | Prefrontal "Off Switch"
- **Definition:** الفصوص الأمامية تعيد تقييم الانفعال وتزن المخاطر والبدائل، فتصحح الاستجابة المندفعة؛ تعمل «مثل أحد الأبوين لإيقاف طفلهما المندفع… أو ينتظر قليلًا قبل الاندفاع»؛ والفص الأمامي الأيسر يعمل «مفتاح إيقاف» للانفعالات المزعجة. الاستجابة القشرية أبطأ «لأنها أكثر تعقلًا وتمييزًا».
- **Book:** Goleman
- **Chapter:** ف2
- **Page:** ص45–48
- **Example:** ★ أم جيسكا: رن التليفون منتصف الليل وابنتها تبيت عند صديقة، فصرخت «جيسكا!» — ثم صوت «أظن أنني طلبت رقمًا خطأ»، فتمالكت الأم أعصابها وسألت بهدوء: «ما الرقم الذي تطلبينه؟» (ص45).
- **Application:** يقدّم فكرة «المساحة» قبل KZ: القشرة تحتاج ثواني لتلحق — كل أدوات الحلقة هدفها «شراء هذه الثواني».
- **Related Concepts:** KB-007, KB-022, KB-027, KB-029
- **Potential Visual:** Animation 2: شخصية «الأب/الأم الهادئ» (القشرة) تمسك يد «الطفل المندفع» (الأميجدالا) قبل أن يعبر الشارع.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]
- **CT#:** 149

### KB-009 · الإنذارات العتيقة | Obsolete Neural Alarms
- **Definition:** الأميجدالا تقارن الحاضر بالماضي بـ«تداعي المعاني»، و«لا تحتاج إلا لبعض عناصر الموقف القليلة… لتبدو مشابهة لخطر سابق»، فتأمرنا بالفعل «بأساليب انطبعت في ذاكرتنا منذ زمن طويل». الذكريات العاطفية «مرشد معيب بالنسبة للحاضر». ذكريات الطفولة المبكرة تبقى «قوالب صامتة من دون كلمات».
- **Book:** Goleman · MoM
- **Chapter:** Goleman ف2؛ MoM Ch.7 «Automatic Thoughts»
- **Page:** Goleman ص40–42؛ MoM p.61–63
- **Example:** ممرضة حرب تنفجر فزعًا من رائحة حفاض متعفن (Goleman ص41). في MoM: فيك يغضب من تقرير شهري، ويكتشف ذكرى أبيه الغاضب من قص العشب؛ ما ساعده: «learning to see the differences between his childhood experiences and his adult experiences» (p.63).
- **Application:** يشرح لماذا رسالة «عايز أشوفك بكرة» قد تفجر ذكرى قديمة (مدير سابق، أب، مدرس) — ويُمهد لفكرة «الزرار» التي يستغلها المتلاعب في المرحلة 7.
- **Related Concepts:** KB-005, KB-042, KB-114
- **Potential Visual:** رسالة واتساب حديثة تتحول ظلالها إلى مشهد قديم باهت (مكتب مدير قديم / صوت أب).
- **Potential Exercise:** «الموقف ده فكّرك بإيه قديم؟» (سؤال داخل Exercise 1).
- **Tag:** [DIRECT SOURCE] (كلا الكتابين)؛ الربط بينهما [INTEGRATED SYNTHESIS]
- **CT#:** 149, 114

### KB-010 · تجمّد الذاكرة العاملة | Working Memory Frozen by Emotion
- **Definition:** «الذاكرة العاملة» في القشرة الأمامية هي «الوظيفة التنفيذية في الحياة الذهنية»؛ الانفعال الشديد (القلق، الغضب) «يخلق تجمدًا عصبيًا» يضعف كفاءتها ⇒ «أنا فقط لا أستطيع أن أفكر تفكيرًا سليمًا». CC يصف أثرًا مشابهًا: الدم يذهب للعضلات الكبيرة وتقل تغذية مناطق التفكير الأعلى، و«your peripheral vision actually narrows».
- **Book:** Goleman · CC
- **Chapter:** Goleman ف2، ف6؛ CC Ch.1، Ch.4
- **Page:** Goleman ص48–49، ص117–118؛ CC p.4، p.50
- **Example:** Goleman في امتحان حساب بالجامعة «تجمدت مع الفزع» (ص117)؛ وعند سماعه كلمة «سرطان» طلب تكرار التعليمات 3–4 مرات (ص237–238).
- **Application:** يجيب عن «ليه مبعرفش أرد وأنا متعصب؟» — ويبرر قاعدة «ما تاخدش قرار مهم وانت في الذروة» (CASE 5 + Shield بند 2).
- **Related Concepts:** KB-004, KB-007, KB-092
- **Potential Visual:** شاشة كمبيوتر «تهنج» عند ارتفاع مؤشر الانفعال؛ نفق رؤية يضيق.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ وصف CC الفسيولوجي = ادعاء مبسط من المؤلفين (يُنسب لهم)
- **CT#:** 148, 4

### KB-011 · المشاعر ضرورية للقرار | Emotions Guide Decisions (Somatic Markers)
- **Definition:** مرضى تلف الدائرة بين الأميجدالا والفص الأمامي — مثل «إليوت» — احتفظوا بذكائهم لكنهم عجزوا عن اتخاذ قرارات بسيطة (موعد) وفقدوا «المخزن… لما يفضله وما يرفضه». «العلامات الجسمانية» (داماسيو) مشاعر دفينة تعمل كـ«إنذار أوتوماتيكي»، و«الأسلوب الأمثل لاتخاذ قرار شخصي صائب يمر عبر مشاعرنا».
- **Book:** Goleman (عن أنطونيو داماسيو)
- **Chapter:** ف2؛ ف4
- **Page:** ص49–50؛ ص80–83
- **Example:** إليوت يروي مآسيه «ببرود شديد» ويتردد بلا نهاية حول موعد (ص80–83).
- **Application:** يمنع سوء الفهم «الذكاء العاطفي = كتم المشاعر». يوازن Shield بند 2: «لا تقرر تحت الخوف» ≠ «تجاهل إحساسك» — الإحساس بعدم الارتياح معلومة (مع KZ «Honor 'gut' feelings» PDF p.103).
- **Related Concepts:** KB-030, KB-113, KB-114
- **Potential Visual:** بوصلة داخل الصدر — تشير لكنها لا تقود العربة.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]؛ الربط بـKZ = [INTEGRATED SYNTHESIS]
- **CT#:** 147

### KB-012 · الذكاء الأكاديمي لا يكفي | IQ ≈ 20% (claim)
- **Definition:** «على أحسن تقدير، فإن معامل الذكاء يسهم في 20% فقط من العوامل التي تحدد النجاح في الحياة» — تقدير Goleman نفسه. ودراسات يذكرها (خريجو هارفارد، دراسة سومرفيل) تُظهر أن قدرات مثل التعامل مع الإحباط والتحكم في الانفعال هي الفارق.
- **Book:** Goleman
- **Chapter:** ف3
- **Page:** ص54–56
- **Example:** 81 طالبًا متفوقًا في إلينوي — واحد من كل أربعة فقط وصل للقمة (ص56).
- **Application:** جزء «لماذا الذكاء العاطفي مهم؟» — يُصاغ بحذر: «Goleman بيقدّر إن…» لا «العلم أثبت إن 80%…».
- **Related Concepts:** KB-001
- **Potential Visual:** كعكة 20/80 مع علامة استفهام صغيرة مكتوب عليها «تقدير المؤلف».
- **Potential Exercise:** —
- **Tag:** [REPORTED IN SOURCE] — ادعاء المؤلف لا حقيقة علمية ثابتة
- **CT#:** 150

### KB-013 · النموذج الخماسي | Five-Part Model
- **Definition:** البيئة + الأفكار + المزاج + السلوك + الاستجابات الجسدية — خمسة أجزاء مترابطة، و«each different part of our lives influences all the others»؛ لذلك «small improvements in any of the areas could contribute to positive change in the others».
- **Book:** MoM (Padesky 1986)
- **Chapter:** Ch.2 «Understanding Your Problems»
- **Page:** p.7–8
- **Example:** بن (78 سنة) بعد مرض زوجته ووفاة صديقه: دوامة هابطة بين الأفكار والانسحاب والجسد (p.5–8). مثال طابور السوبرماركت: «This will take a while. I might as well just relax» مقابل «They shouldn't have such a long line…» (p.2).
- **Application:** الخريطة التي تربط Goleman (المخ/الجسد) بـMoM (الأفكار) وKZ (الملاحظة) وNVC/CC (السلوك مع الآخرين). يُستخدم كـ«لوحة القيادة» في كل الحالات الخمس.
- **Related Concepts:** KB-003, KB-024, KB-038, KB-046
- **Potential Visual:** خماسية متصلة الأضلاع؛ لمس ضلع واحد يحرك الأربعة الأخرى (Animation 3).
- **Potential Exercise:** «املأ الخماسية لموقف امبارح» (نسخة مبسطة من Worksheet 2.1).
- **Tag:** [DIRECT SOURCE]
- **CT#:** 103

### KB-014 · القلق جهاز إنذار يُضبط لا يُفصل | Anxiety as an Alarm to Fine-Tune
- **Definition:** الكر/الفر/التجمد استجابة تكيفية؛ «Anxiety is adaptive when dangers are real and serious… we don't really want to get rid of anxiety completely». القلق = «the body's alarm system»؛ لو الإنذار يرن لما تدخل قطة الحديقة «This wouldn't be a good reason to disconnect your alarm. You would just need either to fine-tune it… or to learn to turn it off quickly». القلق ينشأ حين «the danger we face is greater than our ability to cope».
- **Book:** MoM · Goleman
- **Chapter:** MoM Ch.14 «Understanding Your Anxiety»؛ Goleman ف2، ف6
- **Page:** MoM p.223–224، p.229، p.233–234؛ Goleman ص35، ص125–126
- **Example:** Goleman: منحنى U المقلوب — قلق معتدل = أفضل أداء؛ شديد جدًا = انهيار (ص125–126).
- **Application:** الاستعارة الموحدة للحلقة: **«اضبط الإنذار، ما تفصلوش»** — تربط Goleman بـMoM، وتُستخدم مرة ثانية في Dark EQ: القلق في حضور شخص معين قد يكون إنذارًا حقيقيًا يستحق الفحص.
- **Related Concepts:** KB-005, KB-114, KB-113
- **Potential Visual:** جهاز إنذار منزلي بمقبض «حساسية» يُضبط بين «يرن على كل قطة» و«مطفي».
- **Potential Exercise:** «معادلة القلق»: اكتب الخطر المتصوَّر (1–10) وقدرتك على التعامل (1–10) لموقف يقلقك.
- **Tag:** [DIRECT SOURCE]؛ توحيد الاستعارة بين الكتابين = [INTEGRATED SYNTHESIS]
- **CT#:** 133, 159

### KB-015 · الغضب والصحة — والعداوة عادة تتغير | Anger, Health, and Changeable Hostility
- **Definition:** Goleman ينقل دراسات تربط العداوة المزمنة بأمراض القلب (مثلًا: استرجاع حادثة مغضبة خفّض كفاءة ضخ القلب ~5%)، لكنه يؤكد: «العداوة عادة يمكن تغييرها» — برنامج ويليامز: التنبه لبداية الغضب، تسجيل الأفكار العدائية واستبدالها، والتعاطف «بلسم الغضب». ويحذّر من الطرف المقابل: فكرة أن الناس يشفون أنفسهم بالتفكير الإيجابي تجعلهم «يشعرون بالذنب لأنهم مرضى».
- **Book:** Goleman
- **Chapter:** ف11 «العقل والطب»
- **Page:** ص238–239، ص243–246
- **Example:** مثال المصعد المتأخر: ابحث عن سبب لا إرادي بدل الغضب من «شخص مجهول متخيل» (ص245–246).
- **Application:** «ليه يهمك؟» — دافع صحي بلا تهويل؛ ويؤسس لرسالة الأمان: **لا نقول «فكّر إيجابي وهتخف»**.
- **Related Concepts:** KB-045, KB-048
- **Potential Visual:** قلب ينبض أسرع مع «ترمومتر الغضب»، ثم يهدأ مع أيقونة «أعد التفسير».
- **Potential Exercise:** —
- **Tag:** [REPORTED IN SOURCE] (ارتباطات إحصائية)؛ تحذير Goleman = [DIRECT SOURCE] [SAFETY]
- **CT#:** 178

### KB-016 · المزاج السيئ يصنع تفكيرًا سيئًا | Mood-Congruent Thinking
- **Definition:** «Once a mood is present, we often begin thinking additional thoughts that support and strengthen the mood»، و«the stronger our moods, the more extreme our thinking is likely to be» (MoM). Goleman: الذاكرة المرتبطة بالمزاج تنحاز للسلبي فتنتج قرارات خائفة؛ والقلق «استجابة مفيدة ضلت طريقها».
- **Book:** MoM · Goleman
- **Chapter:** MoM Ch.3؛ Goleman ف6
- **Page:** MoM p.17؛ Goleman ص123–128
- **Example:** الأم القلقة على ابنها في مباراة كرة «تفقد حريتها في الاختيار لأن أفكارها تقهر تفكيرها» (Goleman ص123).
- **Application:** يفسر لماذا تبني 20 سيناريو في 10 دقائق بعد رسالة المدير (الـHook) — المزاج يستدعي أفكارًا تشبهه.
- **Related Concepts:** KB-010, KB-041, KB-049
- **Potential Visual:** كرة ثلج تتدحرج وتكبر — كل فكرة تلصق فكرة من نفس اللون.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ الربط = [INTEGRATED SYNTHESIS]
- **CT#:** 148, 104

### KB-017 · تعريف التقدم: «ترجع أسرع» | Progress = Faster Recovery
- **Definition:** «لا يمكننا غالبًا السيطرة على… متى تجرفنا انفعالاتنا… ولكننا نملك السيطرة على الوقت الذي يستغرقه» (ص88)؛ ولودو: «كلما كان استردادنا لحالتنا الطبيعية أسرع… كان ذلك… إحدى علامات النضج العاطفي» (ص297). MoM: التقدم = تكرار أقل، مدة أقصر، شدة أخف (p.252)؛ و«success did not mean having no anxiety; it meant knowing what to do when she felt anxious» (p.138).
- **Book:** Goleman · MoM
- **Chapter:** Goleman ف5، ف13؛ MoM Ch.11، Ch.15
- **Page:** Goleman ص88، ص297؛ MoM p.138، p.252
- **Example:** ليندا (MoM): النجاح أنها عرفت تعمل إيه وهي قلقانة، مش إن القلق اختفى.
- **Application:** يضبط توقعات الجمهور من البداية: **الهدف مش إنك متتضايقش؛ الهدف إنك ترجع أسرع.** جملة متكررة في الحلقة وفي خطة الأيام السبعة.
- **Related Concepts:** KB-133, KB-135
- **Potential Visual:** رسمان بيانيان للانفعال: قمة عالية تنزل ببطء (قبل)، وقمة مشابهة تنزل بسرعة (بعد) — «المساحة تحت المنحنى».
- **Potential Exercise:** مقياس «التكرار/الشدة/المدة» لموقف غضب هذا الأسبوع (MoM Worksheet 15.1 مبسطة).
- **Tag:** [DIRECT SOURCE]؛ التقاء الكتابين = [INTEGRATED SYNTHESIS]
- **CT#:** 153

---

# المرحلة 2 — NOTICE | لاحظ
*العمود الفقري: Goleman ف4 «اعرف نفسك». الأداة الرئيسية: Kabat-Zinn. داعم: CC (العلامات المبكرة) + MoM (الجسد كدليل).*

### KB-018 · الوعي بالذات | Self-Awareness
- **Definition:** «الانتباه إلى الحالات الداخلية»: أن يلاحظ العقل الخبرة نفسها بما فيها من انفعالات، بطريقة «محايدة تحافظ على تأمل الذات حتى في أثناء العواطف المتهيجة». الفرق الحاسم «بين أن تكون غاضبًا… وأن تدرك… قائلًا: 'أنا أشعر بالغضب…' حتى وأنت في حالة هذا الغضب» — وهي «خطوة أولى تكسب بها السيطرة»؛ إدراك الطفل أنه غاضب «يوفر له… الحرية ليختار عدم إطاعة هذا الشعور».
- **Book:** Goleman
- **Chapter:** ف4 «اعرف نفسك»
- **Page:** ص73–75
- **Example:** ★ الساموراي والراهب: «هذا تمامًا هو الجحيم» — يعيد السيف إلى غمده — «وهذه هي الجنة» (ص73).
- **Application:** افتتاح المرحلة 2. قصة الساموراي تُروى بصريًا، وتصبح «لحظة الجنة» اسمًا للحظة الملاحظة طوال الحلقة.
- **Related Concepts:** KB-019, KB-020, KB-035, KB-058
- **Potential Visual:** رسم حبر ياباني: السيف يخرج — يتجمد — يعود للغمد؛ الكلمتان «جحيم/جنة» تظهران.
- **Potential Exercise:** «قول لنفسك دلوقتي بصوت واطي: أنا حاسس بـ…» (تمرين 10 ثوانٍ).
- **Tag:** [DIRECT SOURCE]
- **CT#:** 151

### KB-019 · أنماط ماير الثلاثة | Mayer's Three Styles
- **Definition:** (1) **الواعون بأنفسهم** — يعرفون مشاعرهم وقت حدوثها (2) **الغارقون** في انفعالاتهم «مغلوبون على أمرهم» (3) **المتقبلون** لمشاعرهم دون محاولة تغييرها (مبتهجون أو مستسلمون لليأس).
- **Book:** Goleman (عن جون ماير)
- **Chapter:** ف4
- **Page:** ص75
- **Example:** «المراقبون» و«الملهيون» في مطبات الطائرة (سوزان ميلر، ص76): المراقب يدقق فيتضخم قلقه، والملهي يشغل نفسه.
- **Application:** شريحة تفاعلية: «انت أنهي نوع؟» — تمهد لأن الوعي مهارة لا صفة ثابتة.
- **Related Concepts:** KB-018, KB-025
- **Potential Visual:** ثلاث شخصيات في قارب وسط موج: واحد يمسك الدفة، واحد تحت الماء، واحد جالس مستسلم.
- **Potential Exercise:** اختيار سريع (Poll) في الوصف/التعليقات.
- **Tag:** [DIRECT SOURCE]
- **CT#:** 151

### KB-020 · اليقظة الذهنية | Mindfulness
- **Definition:** «Mindfulness means paying attention in a particular way: on purpose, in the present moment, and nonjudgmentally.» — تتعلق «above all with attention and awareness, which are universal human qualities»، وKabat-Zinn يؤكد أنها ليست ضد أي معتقد أو دين، ويسميها أيضًا «heartfulness».
- **Book:** KZ
- **Chapter:** «What Is Mindfulness?»؛ Introduction
- **Page:** PDF p.11، p.15–17
- **Example:** ليست طقسًا غريبًا: «simply about being yourself and knowing something about who that is» (p.10).
- **Application:** التعريف الوحيد الذي يُقتبس حرفيًا في المرحلة 2 (مع ترجمة مصرية: «انتباه مقصود، للحظة دي، من غير ما تحكم»). مهم للجمهور المصري: تقديمها كمهارة انتباه لا كممارسة دينية.
- **Related Concepts:** KB-018, KB-021, KB-022, KB-028
- **Potential Visual:** 3 كلمات تظهر بالتتابع: «بقصد» — «دلوقتي» — «من غير حكم».
- **Potential Exercise:** دقيقة انتباه للنَفَس (انظر KB-023).
- **Tag:** [DIRECT SOURCE]؛ الربط بـGoleman: Goleman يذكر عيادة Kabat-Zinn صراحة (ص259) = جسر مصدري
- **CT#:** 72

### KB-021 · الطيار الآلي | Automatic Pilot
- **Definition:** حين نفقد الوعي «we fall into a robotlike way of seeing and thinking and doing»؛ ونفترض أن ما نفكر فيه «the truth… Most of the time, it just isn't so». قلة الوعي تقود إلى «unconscious and automatic actions… often driven by deepseated fears and insecurities». NVC يصف الهدف بعكسه: «Instead of habitual, automatic reactions, our words become conscious responses».
- **Book:** KZ · NVC
- **Chapter:** KZ Introduction، «What Is Mindfulness?»؛ NVC Ch.1
- **Page:** KZ PDF p.9–10، p.16؛ NVC L442
- **Example:** KZ: «Am I awake?», «Where is my mind right now?» — أسئلة فحص لحظي (p.24).
- **Application:** يعرّف المشكلة التي تحلها المرحلة 2: أغلب ردود فعلنا «أوتوماتيك».
- **Related Concepts:** KB-020, KB-027, KB-033
- **Potential Visual:** شخص يمشي والمؤشر فوقه مكتوب «AUTO» — يتحول إلى «MANUAL» حين يلاحظ.
- **Potential Exercise:** «جرس فحص»: 3 مرات النهارده اسأل نفسك «أنا فين دلوقتي؟».
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 73

### KB-022 · التوقف | Stopping
- **Definition:** «Don't just do something, sit there»: الانتقال إلى «being mode» وسؤال: ماذا تشعر؟ ترى؟ تسمع؟ — «There is nothing passive about it». بعد التوقف: «when you're ready, move in the direction your heart tells you to go, mindfully and with resolution». NVC يقول بصيغة شبه متطابقة «Don't just do something, stand there» (عن حضور التعاطف).
- **Book:** KZ · NVC
- **Chapter:** KZ «Stopping»؛ NVC Ch.7
- **Page:** KZ PDF p.20–21؛ NVC L1991–1995
- **Example:** TRY من KZ: توقف واجلس وانتبه لنفسك «for five minutes, or even five seconds».
- **Application:** النواة البصرية لـAnimation 4 «Mindfulness Gap»: التوقف ليس سلبية بل تمهيد لفعل أوضح — يُعاد في Dark EQ: «الهدوء ليس استسلامًا».
- **Related Concepts:** KB-008, KB-027, KB-029, KB-054
- **Potential Visual:** زر «Pause» عملاق بين «المثير» و«الرد»؛ الشريط يتوقف ثم يكمل في اتجاه مختلف.
- **Potential Exercise:** «وقفة 5 ثوانٍ» قبل الرد على أول رسالة مستفزة اليوم.
- **Tag:** [DIRECT SOURCE] (كلا الكتابين)
- **CT#:** 74

### KB-023 · النَّفَس مرساة | Breath as Anchor (+ Balanced Breathing)
- **Definition:** KZ: النفس «anchor line» للانتباه — «not deep breathing or forcing… bare bones awareness»، و«takes no time at all, only a shift in attention». MoM يقدم أداة مختلفة الوظيفة: **التنفس المتوازن** — شهيق 4 عدات وزفير 4 عدات لمدة 4 دقائق، «breathe gently and not take big gulps»، 4 مرات يوميًا لمدة أسبوع للتمكن.
- **Book:** KZ · MoM
- **Chapter:** KZ «Keeping the Breath in Mind»؛ MoM Ch.14
- **Page:** KZ PDF p.25–26؛ MoM p.243
- **Example:** KZ TRY: انتبه لشهيق وزفير واحد كامل فقط.
- **Application:** أداة PAUSE داخل الحلقة. [BOOK DIFFERENCE طفيف]: KZ لا يطلب تغيير النفس (ملاحظة فقط)، وMoM يقدّم تنفسًا منظمًا للتهدئة — نقدّم الاثنين بوضوح: «لاحظ نفسك» (KZ) و«نظّم نفسك» (MoM).
- **Related Concepts:** KB-022, KB-028, KB-092
- **Potential Visual:** دائرة تتمدد 4 ثوانٍ وتنكمش 4 ثوانٍ مع عدّاد على الشاشة.
- **Potential Exercise:** تمرين مباشر داخل الحلقة: دقيقة واحدة 4-4 مع المقدم (يُقال إن MoM يوصي بـ4 دقائق).
- **Tag:** [DIRECT SOURCE] + [BOOK DIFFERENCE]
- **CT#:** 76, 135

### KB-024 · الجسد يعرف أولًا | The Body as First Signal
- **Definition:** علامات جسدية تسبق الوعي بالانفعال: CC «early cues» — جسدية (معدة مشدودة، عيون جافة)، عاطفية، سلوكية (رفع الصوت، الإشارة بالإصبع، صمت مفاجئ) — وهي إشارات «to step back, slow down». MoM: «If you have trouble identifying your moods, pay attention to your body» (أكتاف مشدودة = خوف/ضيق؛ ثقل = حزن)، وعلامات الغضب المبكرة: «shakiness, muscle tension, clenched jaw, chest pressure… clenched fists». KZ: مسح الجسد لملاحظة الضيق في الصدر وما تحته من مشاعر، و«Honor 'gut' feelings». Goleman: برنامج لوكمان يعلّم الأطفال رصد احمرار الوجه وتوتر العضلات كإنذار (ص327).
- **Book:** CC · MoM · KZ · Goleman
- **Chapter:** CC Ch.4؛ MoM Ch.4، Ch.15؛ KZ «Lying-Down Meditation»؛ Goleman ف15
- **Page:** CC p.48–49؛ MoM p.26، p.260–261؛ KZ PDF p.101–103؛ Goleman ص327
- **Example:** Greta (CC p.30–33): المديرة التي تُسأل عن أثاث بـ150 ألف دولار أمام الموظفين — تحمر وتتجمد، ثم تأخذ نفسًا وتسأل «What do I really want here?».
- **Application:** أساس **Exercise 1: Identify Your Trigger** — «جسمك بيقولك قبل عقلك». أقوى نقطة التقاء بين 4 كتب في مرحلة NOTICE.
- **Related Concepts:** KB-003, KB-025, KB-033, KB-092
- **Potential Visual:** مجسم جسم مع «لمبات إنذار» صغيرة (الفك، الصدر، المعدة، القبضة) تضيء بالترتيب.
- **Potential Exercise:** **Exercise 1**: «فين في جسمك بتحس الزعل أول ما يبدأ؟» — المشاهد يختار من الخريطة.
- **Tag:** [DIRECT SOURCE] (4 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 13, 88, 108, 138

### KB-025 · الهدوء الظاهري ≠ غياب الانفعال | Repressors: Calm Face, Aroused Body
- **Definition:** «الكابتون لمشاعرهم» (Repressors): يقولون «أشعر بالهدوء التام» بينما النبض والعرق والضغط مرتفعة — آلية عصبية تحجب المعلومة المزعجة، «ليسوا متظاهرين»؛ «استراتيجية ناجحة… على الرغم من الثمن المجهول الذي يدفعه الوعي بالنفس». CC يصف «low self-monitors»: «I'm not angry!» وهو يرشّ اللعاب.
- **Book:** Goleman · CC
- **Chapter:** Goleman ف5؛ CC Ch.4
- **Page:** Goleman ص112–115؛ CC p.55–56
- **Example:** «Nothing's wrong» بنبرة تقول العكس (CC p.55).
- **Application:** يحذر المشاهد «الهادي دايمًا»: الهدوء الخارجي مش دليل إنك مش متأثر — افحص جسمك.
- **Related Concepts:** KB-024, KB-059
- **Potential Visual:** وجه مبتسم وخلفه رسم قلب يدق بسرعة (شاشة مقسومة).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE] (دراسات واينبرجر/ديفيدسون)
- **CT#:** 157

### KB-026 · لا توقف الموج… تعلّم ركوبه | You Can't Stop the Waves
- **Definition:** «Meditation is neither shutting things out nor off. It is seeing things clearly, and deliberately positioning yourself differently in relationship to them.» الضغوط لا مفر منها، لكن «that does not mean that we have to be victims»؛ لا يمكن وضع «glass plate» على سطح الماء لإيقاف الموج — الكبت يزيد التوتر. الجملة الشهيرة: «You can't stop the waves, but you can learn to surf» (ينقلها KZ عن ملصق لسوامي ساتشيداناندا).
- **Book:** KZ
- **Chapter:** «You Can't Stop the Waves but You Can Learn to Surf»
- **Page:** PDF p.33–34
- **Example:** —
- **Application:** الاستعارة البصرية الرئيسية للمرحلة 2 (وتعود في الختام). تبني جسرًا مع Goleman «الاعتدال لا الكبت».
- **Related Concepts:** KB-030, KB-027, KB-054
- **Potential Visual:** لوح زجاج يحاول الضغط على الموج فيتشقق ← راكب أمواج يتوازن.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] (الجملة منسوبة كما ينسبها KZ)
- **CT#:** 78

### KB-027 · وعاء الوعي: من ردّ الفعل إلى الاستجابة | Awareness Holds Anger — Reacting → Responding
- **Definition:** «Awareness sees the anger; it knows the depth of the anger; and it is larger than the anger. It can therefore hold the anger the way a pot contains food.» — ثم «cook the anger, digest the anger… in changing from an automatic reacting to a conscious responding». والممارسة لا تعني أن تكون «calm when you're not feeling calm» بل أن تحفظ ما يهمك «so that it is not lost… in the heat and reactivity of a particular moment».
- **Book:** KZ
- **Chapter:** «Vision»
- **Page:** PDF p.63–64
- **Example:** KZ يرصد تعبير الغضب في الجسد والنبرة والكلمات دون كبت ولا تنفيس (p.63).
- **Application:** المصدر المباشر لـ**REACTION → RESPONSE** في Animation 4 وفي الإطار النهائي (PAUSE).
- **Related Concepts:** KB-022, KB-029, KB-030, KB-053
- **Potential Visual:** قِدر كبير يحتوي لهبًا أحمر (الغضب) — القدر أكبر من اللهب؛ ينضج ولا ينسكب.
- **Potential Exercise:** «سمِّ الزعل وحطه في القدر»: 3 أنفاس مع جملة «أنا شايف الغضب… وأنا أكبر منه».
- **Tag:** [DIRECT SOURCE]
- **CT#:** 84

### KB-028 · الوعي ليس تفكيرًا — «أرى أفكاري ولست أفكاري» | Awareness ≠ Thought
- **Definition:** KZ: «Awareness is not the same as thought… a vessel which can hold and contain our thinking, helping us to see and know our thoughts as thoughts rather than getting caught up in them as reality»؛ «Meditation does not involve trying to change your thinking by thinking some more. It involves watching thought itself»؛ «If we decide to think positively, that may be useful, but it is not meditation. It is just more thinking.» MoM (ط2) يتبنى المعنى نفسه: «I can see my thoughts and not be my thoughts» (p.129)، و«see your anxious thoughts as simply mental activity rather than as the truth» (p.242).
- **Book:** KZ · MoM
- **Chapter:** KZ «Not to Be Confused with Positive Thinking»؛ MoM Ch.10، Ch.14
- **Page:** KZ PDF p.71–72؛ MoM p.128–129، p.241–242
- **Example:** KZ: الوقوف «خلف الشلال» — ترى الماء ولا يجرفك (p.72).
- **Application:** الجسر بين المرحلتين 2 و3. **[BOOK DIFFERENCE D1]**: الكتابان متفقان أن الفكرة ليست حقيقة؛ الاختلاف في الأولوية: MoM يجعل **فحص الفكرة وتغييرها** أصلًا والمراقبة أداة ضمن أدوات، وKZ يجعل **المراقبة غير الحكمية** هي الممارسة ولا يسعى لاستبدال الفكرة. صياغة الحلقة: «واحد بيقولك افحصها، والتاني بيقولك سيبها تعدّي — وانت محتاج الاتنين حسب الموقف».
- **Related Concepts:** KB-020, KB-041, KB-045, KB-054
- **Potential Visual:** شخص يقف خلف شلال من الكلمات/الأفكار يراها تنهمر ولا يبتل.
- **Potential Exercise:** «سمِّ الفكرة فكرة»: أضف قبلها «أنا عندي فكرة إن…».
- **Tag:** [DIRECT SOURCE] + [BOOK DIFFERENCE D1]
- **CT#:** 85, 122

### KB-029 · الاندفاع لا يلزم أن يصبح فعلًا | Impulses Need Not Become Action
- **Definition:** KZ: حين تجلس في الممارسة «you are not allowing your impulses to translate into action… you do not have to be ruled by them»؛ العادات المتراكمة «can lock us into particular behavior patterns»، و«in one moment… you can 'lose your mind,' commit an irreversible act». Goleman: إدراك الغضب يمنح «الحرية ليختار عدم إطاعة هذا الشعور» (ص74)، وترونجبا: «لا تقهره… ولكن إياك أيضًا أن تطيعه» (ص97–98).
- **Book:** KZ · Goleman
- **Chapter:** KZ «Karma»؛ Goleman ف4، ف5
- **Page:** KZ PDF p.145–147؛ Goleman ص74، ص97–98
- **Example:** KZ: زوجان يمارسان الغضب والعزلة 40 عامًا «wind up imprisoned in anger and isolation» (p.146).
- **Application:** قاعدة الـPAUSE في الإطار النهائي: **الإحساس مسموح، والتنفيذ اختيار**. تُستخدم في CASE 5 (قرار تحت ضغط).
- **Related Concepts:** KB-022, KB-027, KB-030
- **Potential Visual:** سهم من «رغبة» إلى «فعل» يمر عبر بوابة؛ البوابة مكتوب عليها «أنا».
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 96

### KB-030 · الاعتدال لا الكبت — ولا التنفيس | Temperance, Not Suppression (and Not Venting)
- **Definition:** Goleman: «الهدف من ذلك تحقيق التوازن العاطفي وليس قمع العاطفة، لأن لكل شعور قيمته ودلالته»؛ الكبت ← فتور وعزلة، والإفراط ← حالة مرضية. KZ: «suppressing anger… is unhealthy… But it is also unhealthy to vent anger uncontrollably». NVC: لا يُطلب «to squash/swallow anger» بل التعبير عن جوهره كاملًا. CC: «fake it/suppress» يتسرب (فك مشدود، سخرية)؛ الأفضل التأثير في المشاعر بالتفكير فيها.
- **Book:** Goleman · KZ · NVC · CC
- **Chapter:** Goleman ف5؛ KZ «Vision»؛ NVC Ch.10؛ CC Ch.6
- **Page:** Goleman ص86–87؛ KZ PDF p.63؛ NVC L2728؛ CC p.96–97
- **Example:** الطفل الذي يُقال له «كفى» فيتوقف عن الضرب «لكن الغضب يظل يمور بداخله» (Goleman ص74).
- **Application:** رسالة جوهرية: **الذكاء العاطفي مش إنك تكتم ولا إنك تفرّغ.** أقوى نقطة التقاء (4 من 5 كتب).
- **Related Concepts:** KB-026, KB-027, KB-048, KB-053
- **Potential Visual:** ثلاث زجاجات مياه غازية: مغلقة بإحكام (تنفجر)، مفتوحة بعنف (تفور وتضيع)، تُفتح ببطء (هادئة).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] (4 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 152

### KB-031 · الصبر: انتظر حتى يترسب الطين | Patience — Let the Mud Settle
- **Definition:** «Scratch the surface of impatience and what you will find lying beneath it… is anger»؛ «possible even to hurry patiently». ينقل KZ سؤال لاو-تسو: «Do you have the patience to wait till your mud settles and the water is clear?»؛ و«It's not that feelings of anger don't arise. It's that the anger can be used, worked with, harnessed». وينقل ما معناه عن الدالاي لاما: «They have taken everything from us; should I let them take my mind as well?» (يصوغه KZ بـ«something to the effect that»).
- **Book:** KZ
- **Chapter:** «Patience»؛ «Going Upstairs»
- **Page:** PDF p.44–47، p.131–132
- **Example:** KZ TRY: «try not to push the river… listen… If the river tells you something, then do it… Then pause».
- **Application:** يدعم قاعدة «ما تردش في الذروة» (CASE 4 واتساب) — ومعه KZ «Going Upstairs»: «hardly ever an outward hurry. Only an inner one»، وTRY: «Notice the inner feelings which push you toward the telephone or the doorbell on the first ring. Why does your response time have to be so fast» (PDF p.131–132). وجملة الدالاي لاما تُستعاد في Dark EQ: «ما تخليهوش ياخد عقلك كمان» — مع ذكر أنها صياغة KZ التقريبية.
- **Related Concepts:** KB-022, KB-092, KB-129
- **Potential Visual:** كوب ماء عكر يترسب طينه تدريجيًا حتى يصفو (Animation قصيرة 5 ثوانٍ).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] (اقتباسات منقولة داخل KZ)
- **CT#:** 79, 94

### KB-032 · نظارات الحلم | Dream Glasses
- **Definition:** «look at other people and ask yourself if you are really seeing them or just your thoughts about them… dream glasses… dream husband, dream wife… dream colleagues». وفي «Direct Contact»: «we often see our thoughts, or someone else's, instead of seeing what is right in front of us».
- **Book:** KZ
- **Chapter:** «Waking Up»؛ «Direct Contact»
- **Page:** PDF p.30، p.120–121
- **Example:** علماء الفلك الذين لم ينظروا مباشرة في التلسكوب (قصة وايسكوف، p.120).
- **Application:** الجسر من NOTICE (نفسي) إلى EMPATHIZE (الآخر) — وإلى CASE 2 (الزوجين): «انت شايف مراتك ولا شايف فكرتك عنها؟».
- **Related Concepts:** KB-043, KB-047, KB-058
- **Potential Visual:** نظارة تُخلع فتتحول صورة «الزوج الغاضب» إلى إنسان متعب.
- **Potential Exercise:** «اكتب صفة واحدة شايفها في حد قريب… وبعدين اكتب فعل واحد شفته بعينك النهارده».
- **Tag:** [DIRECT SOURCE]
- **CT#:** 77

### KB-033 · اعرف مثيرك | Know Your Triggers
- **Definition:** KZ TRY: لاحظ «consequences of your more mindless and automatic behaviors, especially when they are provoked by pressures stemming from work or home life… What triggers them? Are you ready to hold them in awareness as they grip you by the throat». MoM Worksheet 11.1 يعدد مواقف المشاعر القوية ومنها «someone criticizes you… people are late… someone tries to take advantage of you». CC: لاحظ «the moment conversation turns crucial».
- **Book:** KZ · MoM · CC
- **Chapter:** KZ «Not Practicing Is Practicing»؛ MoM Ch.11؛ CC Ch.4
- **Page:** KZ PDF p.106؛ MoM p.141–142؛ CC p.47–49
- **Example:** Goleman: شخص «أزعجه لقاء وقح… في ساعة مبكرة… يعيش في حالة نكد لساعات» حتى يلفت نظره أحد (ص84–85).
- **Application:** **Exercise 1: Identify Your Trigger** (الجزء ب): المشاهد يكتب أعلى 3 مثيرات عنده.
- **Related Concepts:** KB-009, KB-024, KB-042
- **Potential Visual:** قائمة «أزرار» على لوحة تحكم: «نقد قدام الناس» / «تأخير» / «تجاهل» / «استغلال».
- **Potential Exercise:** **Exercise 1** (نسخة كاملة): «الزرار ← الجسم ← الفكرة الأولى ← اللي عملته».
- **Tag:** [DIRECT SOURCE]؛ صيغة التمرين = [INTEGRATED SYNTHESIS]
- **CT#:** 89, 13

### KB-034 · تدرّب قبل الأزمة | Practice Before the Crisis
- **Definition:** KZ: «you can't just think that you understand how to be mindful, and save using it for only those moments when the big events hit. They contain so much power they will overwhelm you instantly»، و«If there is no mindfulness… now… how likely is it that it will magically appear later, under stress or duress?». Goleman: الاستجابة الجديدة تُجرَّب «في أثناء المواجهات الخفيفة غير المتأزمة» حتى تصبح تلقائية. CC: ابدأ بمحادثة «medium-risk».
- **Book:** KZ · Goleman · CC
- **Chapter:** KZ «Posture»، «Karma»؛ Goleman ف9؛ CC Ch.12
- **Page:** KZ PDF p.81، p.147؛ Goleman ص211–212؛ CC p.221–222
- **Example:** KZ: «Five minutes of formal practice can be as profound or more so than forty-five minutes» (p.85).
- **Application:** المبرر المصدري لخطة الأيام السبعة وللتمارين القصيرة داخل الحلقة.
- **Related Concepts:** KB-133, KB-134
- **Potential Visual:** سبّاح يتدرب في حمام سباحة هادئ قبل أن يدخل البحر.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 174, 43

---

# المرحلة 3 — NAME + REFRAME | سمِّ وأعِد التأطير
*العمود الفقري: Goleman ف5 «عبيد العاطفة» + ف6 «القدرة المسيطرة». الأداة الرئيسية: Mind Over Mood. داعم: CC ف6 «Master My Stories» + NVC ف4–5، 9–10.*

### KB-035 · تسمية المشاعر — محو الأمية العاطفية | Naming Feelings / Emotional Literacy
- **Definition:** تحديد الانفعال وتسميته يتطلب مناطق اللغة في القشرة (Goleman ص73–74). **الألكسيثيميا**: من «يفتقرون للكلمات التي تعبر عن مشاعرهم» فيعيشونها كأعراض جسدية (ص77–80). أقوى دليل تطبيقي عند Goleman: دراسة 900+ تلميذة — أقوى علامة لاضطرابات الأكل ضعف إدراك المشاعر؛ «لا يعرفن ما إذا كن غاضبات أو قلقات أو مكتئبات، إنما يشعرن فقط بعاصفة انفعالية» (ص337–341). CC: «many people are emotionally illiterate… expand your emotional vocabulary». NVC: «Our repertoire of words for calling people names is often larger than our vocabulary of words to clearly describe our emotional states».
- **Book:** Goleman · CC · NVC
- **Chapter:** Goleman ف4، ف15؛ CC Ch.6؛ NVC Ch.4
- **Page:** Goleman ص73–80، ص337–341؛ CC p.103–104؛ NVC L965
- **Example:** Goleman ينقل عن هنري روث: «إذا استطعت أن تجد كلمات لما تشعر به، فأنت نفسك» (ص79–80).
- **Application:** افتتاح المرحلة 3 و**Exercise 2: Name the Emotion**. [SAFETY]: نذكر نتيجة دراسة اضطرابات الأكل كمبدأ فقط، دون تفاصيل سلوكيات الأكل.
- **Related Concepts:** KB-036, KB-037, KB-018
- **Potential Visual:** «عجلة المشاعر» بالعامية المصرية (زعلان ← محبط / مجروح / متضايق / مكسوف…).
- **Potential Exercise:** **Exercise 2**: «بدل "متضايق"… اختار كلمة أدق من العجلة» + تقييم الشدة (KB-037).
- **Tag:** [DIRECT SOURCE] (3 كتب) + [REPORTED IN SOURCE] + [SAFETY]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 22, 185

### KB-036 · المزاج كلمة واحدة — والجملة فكرة | A Mood Is One Word; a Sentence Is a Thought
- **Definition:** MoM: «As a general rule, moods can be identified in one word… If it takes you more than one word to describe a single mood, you may be describing a thought»؛ «Part of developing the ability to identify your moods is learning to distinguish your moods from your thoughts» — «I feel like I want to be alone» فكرة، والمزاج = حزن. NVC بنفس المنطق: «I feel that/like/as if…» = أفكار لا مشاعر؛ وكلمات مثل **abandoned, betrayed, manipulated, ignored, pressured, used** «تفسيرات تتنكر في شكل مشاعر»؛ حتى «I feel my boss is being manipulative» ليست شعورًا.
- **Book:** MoM · NVC
- **Chapter:** MoM Ch.4؛ NVC Ch.4
- **Page:** MoM p.25–27؛ NVC L997–1063
- **Example:** فيك (MoM p.26): كان يصف حالته بـ«uncomfortable/numb/out of control»؛ عندما ميّز، اتضح أن القلق مرتبط بـ«I'm losing control» والغضب بـ«This is not fair – I deserve more respect».
- **Application:** قاعدة «كلمة واحدة» تُعلّم في Exercise 2. وملاحظة NVC عن كلمة «manipulated» تُستخدم في Dark EQ: «حاسس إني مستغَل» = تفسير يحتاج فحصًا (لا إنكارًا) — انظر KB-114.
- **Related Concepts:** KB-035, KB-043, KB-114
- **Potential Visual:** جملتان على الشاشة: «حاسس إنه بيستغلني» (أحمر: فكرة) ← «حاسس بـ: خوف، ضيق» (أخضر: شعور).
- **Potential Exercise:** «شعور ولا فكرة؟» — 6 جمل سريعة والمشاهد يرد في التعليقات (مستلهم من MoM Worksheet 6.1، بأمثلة جديدة).
- **Tag:** [DIRECT SOURCE] (الكتابان)؛ التطابق = [INTEGRATED SYNTHESIS]
- **CT#:** 107, 49

### KB-037 · قياس شدة المزاج 0–100 | Rating Mood Intensity
- **Definition:** تقييم كل مزاج من 0 («Not at all») إلى 100 («Most I've ever felt») لمتابعة التقلب، وربط المواقف والأفكار بالتغير، وقياس فعالية الاستراتيجيات. «The presence of strong moods is our first clue that something important is happening».
- **Book:** MoM
- **Chapter:** Ch.4
- **Page:** p.29–30
- **Example:** ماريسا: «Overwhelmed 95% ← 40%»، «Depressed 85% ← 80%» (p.41–43) — أمانة: التحسن قد يكون صغيرًا.
- **Application:** «الترمومتر» البصري الذي يظهر فوق الشخصيات في كل الحالات الخمس (قبل/بعد).
- **Related Concepts:** KB-035, KB-046, KB-092
- **Potential Visual:** ترمومتر رأسي بجانب كل شخصية؛ الرقم يتغير مع كل خطوة.
- **Potential Exercise:** جزء من Exercise 2: «اسم الشعور + رقمه».
- **Tag:** [DIRECT SOURCE]
- **CT#:** 109

### KB-038 · التفسير يصنع الشعور | Different Interpretations → Different Moods
- **Definition:** «the moods we experience often depend upon our thoughts. Different interpretations of an event can lead to different moods». و«it is important to identify what you are thinking and to check out the accuracy of your thoughts before acting».
- **Book:** MoM
- **Chapter:** Ch.3 «It's the Thought That Counts»
- **Page:** p.16–17
- **Example:** ★ أليكس في الحفلة لا ينظر إليك: «Alex is rude» ← ضيق؛ «Alex doesn't find me interesting» ← حزن؛ «Alex seems shy» ← اهتمام (p.16). NVC: اللكمة في الأنف مرتين — ملصق «spoiled brat» ← غضب، و«pathetic creature» ← لا غضب (L2768–2772). Goleman: غضب الطريق: «هذا الولد ابن ال…» مقابل «ربما لم ير سيارتي… حالة طوارئ» (ص90).
- **Application:** قلب Animation 3 «Emotion → Thought → Behavior»، ويُطبَّق مباشرة على الـHook (رسالة المدير) وCASE 4 (واتساب).
- **Related Concepts:** KB-039, KB-040, KB-041, KB-013
- **Potential Visual:** موقف واحد (شخص لا يرد السلام) ← 3 فقاعات تفكير ← 3 وجوه مختلفة (Split-screen).
- **Potential Exercise:** «موقف واحد… 3 تفسيرات»: المشاهد يكتب 3 تفسيرات لرسالة «عايز أشوفك بكرة».
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 104

### KB-039 · المثير لا السبب | Stimulus vs. Cause
- **Definition:** NVC: «what others say and do may be the stimulus, but never the cause, of our feelings»؛ «We are never angry because of what others say or do» — سبب الغضب في التفكير (اللوم/الحكم). CC: «others don't make you mad. You make you mad» (Claim One)، ثم «act on emotions or be acted on by them» (Claim Two). KZ: «Notice how even speaking of something 'making' you angry surrenders your power to others». Epictetus (عنوان فصل في NVC): «People are disturbed not by things, but by the view they take of them».
- **Book:** NVC · CC · KZ
- **Chapter:** NVC Ch.5، Ch.10؛ CC Ch.6؛ KZ «Cat-Food Lessons»
- **Page:** NVC L1147–1151، L2732–2748؛ CC p.94–95؛ KZ PDF p.160
- **Example:** NVC: التأخر نفسه قد يسبب أذى أو إحباطًا أو ارتياحًا حسب الاحتياج (L2748–2756).
- **Application:** مبدأ «مسؤوليتي عن شعوري» في المرحلة 3. **تحفظ إلزامي**: يُقدَّم مع [BOOK DIFFERENCE D3] — MoM وGoleman يريان أن الغضب قد يكون استجابة صحية للإساءة (KB-116)، وGoleman يصف ردودًا انفعالية تسبق التفكير (KB-006). الصياغة: «الموقف بيدوس الزرار… لكن تفسيرك بيحدد قد إيه الزرار ده بيولّع» — وليس «انت السبب لو حد أذاك».
- **Related Concepts:** KB-038, KB-040, KB-103, KB-116
- **Potential Visual:** زرار (المثير) متصل بسلك يمر عبر «صندوق التفسير» قبل أن يصل للمبة (الشعور).
- **Potential Exercise:** حوّل «هو خلاني أتعصب» إلى «أنا اتعصبت لما… لأني كنت محتاج…».
- **Tag:** [DIRECT SOURCE] + [BOOK DIFFERENCE D3]
- **CT#:** 19, 50

### KB-040 · مسار الفعل: نرى ← نحكي قصة ← نشعر ← نفعل | Path to Action
- **Definition:** «Just after we observe what others do and just before we feel some emotion about it, we tell ourselves a story»: See/Hear → Tell a Story → Feel → Act. «Storytelling typically happens blindingly fast» — لكن إن لم تكن تغضب **دائمًا** حين يُضحك عليك، فالاستجابة ليست حتمية. «once they're told, the stories control us». تتبع المسار عكسيًا: هل أنا في صمت أم عنف؟ ماذا أشعر؟ ما القصة؟ ما الدليل؟
- **Book:** CC
- **Chapter:** Ch.6 «Master My Stories»
- **Page:** p.98–102
- **Example:** ماريا ولويس (p.95–96): زميلها تولّى العرض وقابل المدير وحده ← قصة «نادي الرجال» ← سخرية.
- **Application:** النسخة «العملية» من KB-038 للمرحلة 6. **[BOOK DIFFERENCE D6 (محسوم)]**: CC يجعل القصة قبل الشعور، وGoleman يصف ردًا انفعاليًا قد يسبق التفكير؛ CC نفسه يعترف أن القصة «blindingly fast» — نعرض النموذجين كطبقتين: إنذار سريع (Goleman) + قصة تُغذيه أو تُطفئه (CC/MoM).
- **Related Concepts:** KB-006, KB-038, KB-047, KB-089
- **Potential Visual:** 4 محطات مترو تضيء بالترتيب؛ ثم قطار يرجع للخلف في «تتبع المسار».
- **Potential Exercise:** «ارجع بالمسار»: من اللي عملته ← لحد اللي شفته فعلًا.
- **Tag:** [DIRECT SOURCE] + [BOOK DIFFERENCE D6]
- **CT#:** 20, 21

### KB-041 · الأفكار التلقائية وأسئلة كشفها | Automatic Thoughts
- **Definition:** «the words and images that pop into our heads throughout the day»؛ «Thoughts often occur rapidly, automatically, and just out of our awareness». «If we can identify the thoughts we are having, our moods usually make perfect sense»؛ «Awareness is the first step toward change». أسئلة الكشف: «What was going through my mind just before I started to feel this way?»؛ قلق: «What am I afraid might happen?»؛ غضب: «What does this mean about the other person(s)…?»؛ اكتئاب: «What does this mean about me?». Goleman ينقل المفهوم نفسه عن آرون بيك (ص197–198): حوار منطوق وآخر صامت موازٍ.
- **Book:** MoM · Goleman
- **Chapter:** MoM Ch.3، Ch.7؛ Goleman ف9
- **Page:** MoM p.19، p.50–56؛ Goleman ص197–198
- **Example:** فيك وتغيير زيت السيارة: «Fine! Why don't you just get yourself another husband!» — الأفكار الحقيقية: «She doesn't appreciate how hard I'm trying… she's never happy with me» (MoM p.50–52).
- **Application:** **Exercise 3: Automatic Thought**. جسر مصدري صريح: Goleman يستشهد ببيك مؤسس العلاج المعرفي ⇒ MoM امتداد طبيعي للعمود الفقري.
- **Related Concepts:** KB-042, KB-046, KB-051, KB-016
- **Potential Visual:** فقاعة كلام (ما نقوله) وتحتها فقاعة شفافة (ما نفكر فيه) تظهر عند «تفعيل أشعة X».
- **Potential Exercise:** **Exercise 3**: «إيه اللي كان بيعدي في دماغك قبل ما تتضايق بثانية؟» — 3 أسئلة الكشّاف.
- **Tag:** [DIRECT SOURCE]؛ الجسر = [DIRECT SOURCE] (Goleman يذكر بيك)
- **CT#:** 112, 113, 171

### KB-042 · الفكرة الساخنة | Hot Thought
- **Definition:** بين كل الأفكار التلقائية فكرة «ساخنة» — كالسلك المكهرب (hot wire) — تحمل أكبر شحنة وترتبط بأقوى مزاج؛ هي التي تُفحص.
- **Book:** MoM
- **Chapter:** Ch.7
- **Page:** p.61–63
- **Example:** فيك والتقرير الشهري: «Why is she reading it here?» 10% ← «I bet the other salespeople did better» 80% ← «I'll get fired» 90% (الساخنة).
- **Application:** في كل Case: نحدد «الفكرة الساخنة» ونلوّنها بالأحمر على الشاشة.
- **Related Concepts:** KB-041, KB-044, KB-009
- **Potential Visual:** أسلاك متعددة؛ واحد يتوهج أحمر ويصدر شرارة.
- **Potential Exercise:** من أفكار Exercise 3: «أنهي فكرة لو اتشالت الزعل يقل أكتر؟».
- **Tag:** [DIRECT SOURCE]
- **CT#:** 114

### KB-043 · الحقيقة مقابل التفسير | Facts vs. Interpretations (Observation vs. Evaluation)
- **Definition:** MoM: «Facts are generally things that everyone would agree on… Interpretations are things people looking at the same situation might disagree about» — «The expression on Judy's face changed» حقيقة، «She's always giving me negative looks» تفسير؛ و«Peter stared at me and thought I was crazy» ليست حقيقة. CC: القصة ليست حقيقة؛ اختبار الحقيقة: «can you see or hear it?»؛ الكلمات «الساخنة» (scowl, sarcastic) مقابل «Her eyes pinched shut and her lips tightened». NVC: فصل الملاحظة عن التقييم؛ 7 طرق يختلطان بها؛ «always/never» مبالغات تستفز الدفاع.
- **Book:** MoM · CC · NVC
- **Chapter:** MoM Ch.8؛ CC Ch.6؛ NVC Ch.3
- **Page:** MoM p.72–73، p.85؛ CC p.105–106؛ NVC L766–873
- **Example:** NVC: «Doug procrastinates» ← «Doug only studies for exams the night before» (L818–832).
- **Application:** **أقوى نقطة التقاء في المصادر الخمسة** (3 كتب بلا اقتباس متبادل). تُعلَّم مرة واحدة وتُستخدم في: NAME، COMMUNICATE (الملاحظة في NVC)، HANDLE CONFLICT (Share your facts في STATE)، وPROTECT (الدرع بند «الحقائق» والتوثيق).
- **Related Concepts:** KB-044, KB-072, KB-089, KB-114, KB-127
- **Potential Visual:** «كاميرا المراقبة»: ما تسجله الكاميرا (حقيقة) مقابل تعليق المعلّق (تفسير) — Split-screen.
- **Potential Exercise:** «حقيقة ولا تفسير؟» — 8 جمل من حياة العمل والبيت (أمثلة أصلية، على نمط NVC Exercise 1).
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 116, 23, 48

### KB-044 · أين الدليل؟ | Where's the Evidence?
- **Definition:** «the most important question in CBT: 'Where's the evidence?'». عامل الأفكار الساخنة «as hypotheses, or guesses». «When we have negative automatic thoughts, we usually dwell on data that confirm our conclusions»؛ والبحث عن الدليل المعاكس «one secret to reducing the intensity of our moods». أسئلة الدليل المعاكس: ماذا أقول لصديقي لو فكّر هكذا؟ ماذا يقول لي من يحبني؟ تفاصيل صغيرة أتجاهلها؟ «Five years from now…»؟ هل أقفز لاستنتاج؟ «Am I blaming myself for something over which I do not have complete control?». Goleman (عن بيك): رصد الأفكار المسمومة و«عدم تصديقها عن وعي» واستحضار شواهد تشكك فيها.
- **Book:** MoM · Goleman
- **Chapter:** MoM Ch.8؛ Goleman ف9
- **Page:** MoM p.69–75؛ Goleman ص208–209
- **Example:** Goleman: «إنه… دائمًا أناني» ← «حسن، إنه يبدي اهتمامه بي أحيانًا على الرغم مما فعله الآن» (ص209).
- **Application:** **Exercise 4: Reframe** (الجزء أ). سؤال «هل ألوم نفسي على ما لا أتحكم فيه؟» يعود في Dark EQ (لوم الذات عند من تعرّض للتلاعب — KB-119).
- **Related Concepts:** KB-043, KB-045, KB-046, KB-119
- **Potential Visual:** ميزان عدالة — كفة «أدلة مع» وكفة «أدلة ضد»؛ القاضي = أنت.
- **Potential Exercise:** **Exercise 4 (أ)**: «اكتب دليلين مع الفكرة الساخنة، ودليلين ضدها».
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 117, 171

### KB-045 · الفكرة المتوازنة بـ«و» — ليست تفكيرًا إيجابيًا | Balanced Thought — Not Positive Thinking
- **Definition:** لخّص الأدلة المؤيدة في جملة والمعارضة في جملة واربطهما بـ«and». «Alternative or balanced thinking… is not merely the substitution of a positive thought for a negative thought. Positive thinking tends to ignore negative information and can be as damaging as negative thinking». و«positive thinking is not a solution to life's problems… can lead us to overlook information that might be important» (p.23). **«The goal of a Thought Record is not to eliminate emotions»** بل نظرة أوسع (p.106). KZ يرفض التفكير الإيجابي كبديل للوعي (p.72)، وGoleman يحذر من «التفاؤل المفرط في السذاجة» (ص130) ومن أيديولوجية «إسعاد النفس» للشفاء (ص238).
- **Book:** MoM · KZ · Goleman
- **Chapter:** MoM Ch.3، Ch.9؛ KZ «Not Positive Thinking»؛ Goleman ف6، ف11
- **Page:** MoM p.23، p.98–106؛ KZ PDF p.72؛ Goleman ص130، ص238
- **Example:** «I've made some mistakes as a parent, and yet all parents make mistakes. Making some mistakes doesn't make me a bad parent» — وليس «I'm a great parent» (MoM p.98–99). بن: الفرق بين الفكرة المتوازنة و«They need me more than ever» (إيجابية زائفة) و«but what do I care?» (تبرير) (p.101–103).
- **Application:** رسالة جوهرية تُقال بوضوح: **«مش "فكّر إيجابي"… "فكّر كامل"»**. قالب مصري: «صحيح إن… وكمان…». **Exercise 4 (ب)**.
- **Related Concepts:** KB-044, KB-028, KB-054, KB-015
- **Potential Visual:** ثلاث نظارات: سوداء (سلبي)، وردية (إيجابي زائف)، شفافة (متوازن).
- **Potential Exercise:** **Exercise 4 (ب)**: اكتب فكرتك المتوازنة بصيغة «صحيح إن … وكمان …» وقيّم تصديقك لها 0–100.
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 105, 119

### KB-046 · سجل الأفكار ذو الأعمدة السبعة | Seven-Column Thought Record
- **Definition:** (1) الموقف: من؟ ماذا؟ متى؟ أين؟ (2) المزاج + التقييم 0–100 (3) الأفكار التلقائية/الصور + تحديد الساخنة (4) أدلة تؤيد (5) أدلة لا تؤيد (6) فكرة بديلة/متوازنة + تقييم تصديقها (7) إعادة تقييم المزاج. «Doing a Thought Record is not a test»؛ «The Thought Record is not intended to disprove your hot thought, but to investigate it». بعد 20–40 سجلًا يبدأ كثيرون التفكير المتوازن تلقائيًا [REPORTED IN SOURCE].
- **Book:** MoM (Padesky 1983)
- **Chapter:** Ch.6–9
- **Page:** p.40–43، p.63، p.106، p.112
- **Example:** سجل فيك مع جودي في اختيار فيلم: Angry 99%, Hurt 95% — «She never cares about what I want to do… She always has to be in control» (p.45).
- **Application:** الأداة المركزية للمرحلة 3؛ تُبسّط في الحلقة إلى «سجل مصري من 5 خانات» (الموقف — الشعور ورقمه — الفكرة الساخنة — الدليل مع/ضد — الفكرة المتوازنة ورقم الشعور الجديد) مع ذكر أن الأصل 7 أعمدة. أمانة زمنية: 7 أيام بداية لا إتقان.
- **Related Concepts:** KB-037, KB-041, KB-042, KB-044, KB-045
- **Potential Visual:** Animation 5 «Cognitive Restructuring»: جدول يمتلئ عمودًا عمودًا، والترمومتر ينزل في النهاية.
- **Potential Exercise:** قالب قابل للتحميل (Handout) + تطبيق مباشر على CASE 4.
- **Tag:** [DIRECT SOURCE]؛ التبسيط الخماسي = [INTEGRATED SYNTHESIS]
- **CT#:** 110, 111

### KB-047 · القصص الذكية الثلاث — وأكمل القصة | Victim, Villain, Helpless Stories
- **Definition:** CC: قصة **الضحية** («It's not my fault»)، قصة **الشرير** («It's all your fault» + الملصقات)، قصة **العاجز** («There's nothing else I can do»). «We tell a clever story when we want self-justification more than results». التصحيح: الضحية ← «Am I pretending not to notice my role?»؛ الشرير ← «Why would a reasonable, rational, and decent person do what this person is doing?»؛ العاجز ← «What do I really want?…». **توازن ضروري**: «there is such a thing as an innocent victim… it's a sad fact, not a story» (p.107)، و«Sometimes the stories we tell are accurate. The other person is trying to cause us harm… It's not common, but it can happen» (p.109)، وسؤال الأنسنة «is not to excuse others» (p.114). Goleman (عن بيك): فكرتا الزيجات المضطربة «أنا ضحية بريئة» و«أنا على حق في غضبي» تتأكدان ذاتيًا بانتقاء الأدلة (ص197–199).
- **Book:** CC · Goleman
- **Chapter:** CC Ch.6؛ Goleman ف9
- **Page:** CC p.106–115؛ Goleman ص197–199
- **Example:** ماريا تعيد قصتها: لويس يتكلم أكثر حين يتوتر ⇒ اتفقا على تقسيم العرض (CC p.115–117).
- **Application:** أداة للمرحلة 3 و6، **وحجر أساس لتوازن Dark EQ**: الكتاب الذي يعلّمك أن تشك في قصة «الشرير» هو نفسه يقول إن الأذى المقصود موجود أحيانًا ⇒ الحل: الدليل والنمط (KB-094)، لا الإنكار ولا الاتهام.
- **Related Concepts:** KB-040, KB-044, KB-064, KB-094, KB-113
- **Potential Visual:** ثلاث أقنعة مسرحية (ضحية — شرير — عاجز) تسقط لتكشف وجوهًا بشرية.
- **Potential Exercise:** «أنهي قصة من التلاتة بتحكيها لنفسك دلوقتي؟» + سؤال التصحيح.
- **Tag:** [DIRECT SOURCE] (الكتابان)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 24, 25, 26, 171

### KB-048 · دورة الغضب: الغضب يبني على الغضب — والتهدئة | Anger Builds on Anger; Cooling Off
- **Definition:** زيلمان: المحفز العام للغضب الإحساس بالخطر، ومنه «التهديد الرمزي للكرامة» (معاملة بوقاحة أو ظلم أو إهانة). موجة أولى تدوم دقائق، واستثارة تدوم ساعات أو أيامًا وتخفض عتبة الغضب ⇒ «الغضب يعزز الغضب». الغضب أصعب الأمزجة في الهروب منه لأن «المونولوج الداخلي… مبرر أخلاقيًا». التهدئة: (1) **تحدي الأفكار مبكرًا** — المعلومة المخففة («كان تحت ضغط الامتحانات») تنجح في الغضب المتوسط **لا في الذروة** (2) **التبريد**: مشي، رياضة، استرخاء، إلهاء — والاجترار أثناء التبريد لا يفيد. **خرافة التنفيس**: التنفيس يطيل الغضب.
- **Book:** Goleman
- **Chapter:** ف5 «عبيد العاطفة»
- **Page:** ص90–98
- **Example:** يوم عمل صعب ← صراخ في الأطفال مساءً (ص92). سائق التاكسي: «على الأقل لكي تنفّس» (ص97).
- **Application:** يشرح لماذا «Reframe» يجب أن يأتي **مبكرًا**، ولماذا في الذروة نحتاج PAUSE أولًا (يربط المرحلة 2 بـ3). يُستخدم في CASE 1 وCASE 2.
- **Related Concepts:** KB-030, KB-092, KB-116, KB-045
- **Potential Visual:** موجات متراكبة تعلو (كل استفزاز جديد يبدأ من ارتفاع الموجة السابقة).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE] (أبحاث زيلمان وتايس)
- **CT#:** 154

### KB-049 · القلق كتعويذة — وتحدي أفكاره | Worry as Magic Charm
- **Definition:** القلق «بروفة» لمواجهة خطر، والقلق المزمن نوبة صغيرة، و«تعويذة سحرية» يظن صاحبها أنها تمنع السوء؛ العلاج: الوعي بالعلامات المبكرة، الاسترخاء، والتحدي النشط («هل من المحتمل جدًا…؟») (Goleman). MoM: جابرييلا: «If I worry, then I can anticipate bad things and protect my children» — وأختها: «Things I worried about in the past didn't happen, and the bad things that happened, I never thought to worry about!» (p.145–147). أفكار القلق: «We overestimate danger and underestimate our ability to cope».
- **Book:** Goleman · MoM
- **Chapter:** Goleman ف5؛ MoM Ch.7، Ch.11، Ch.14
- **Page:** Goleman ص98–104؛ MoM p.55–56، p.145–147
- **Example:** «الأم القلقة» — تجربة MoM «افعل العكس»: ليلة ألعاب بدل القلق ← «I don't need to worry constantly to be a good mother».
- **Application:** CASE 5 (قرار تحت ضغط) وCASE 4 (واتساب): «السيناريوهات العشرين» في الـHook.
- **Related Concepts:** KB-014, KB-016, KB-051
- **Potential Visual:** تميمة معلقة مكتوب عليها «لو قلقت هتحمي» ← تتشقق.
- **Potential Exercise:** «أسوأ / أحسن / الأرجح» (MoM p.100) لسيناريو يقلقك.
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 155

### KB-050 · الاجترار والحزن — والانتصار الصغير | Rumination, Sadness, Small Victories
- **Definition:** قدر من الحزن مفيد (يتيح التأمل بعد الفقد)؛ العامل الحاسم في استمراره هو **الاجترار** (نولن-هوكسمان)؛ العزلة تزيده. أنجح الاستراتيجيات حسب تايس: «انتصار بسيط أو نجاح سهل»، ومساعدة الآخرين من أقواها وأندرها، و«تغيير الإطار المعرفي» (Goleman). MoM: التنشيط السلوكي — أنشطة ممتعة، إنجاز، مواجهة ما نتجنبه، متسقة مع القيم؛ و«motivation often follows doing something rather than coming first». وظيفة الحزن: «it can help us understand what is important to us».
- **Book:** Goleman · MoM
- **Chapter:** Goleman ف5؛ MoM Ch.13
- **Page:** Goleman ص105–112؛ MoM p.189، p.201–217
- **Example:** بن: «When I'm alone and just sitting around, I tend to dwell on things and feel worse» (MoM p.208–209).
- **Application:** يدعم يوم «Reflect» في الخطة وفكرة «ابدأ حتى لو مش حاسس». [SAFETY]: نفرّق بين الحزن العادي والاكتئاب؛ نحيل لمتخصص عند الاستمرار (MoM: إن لم تتحسن الدرجات خلال 6 أسابيع «get help from a health care professional»، p.193). لا نعرض وصف ستايرون لأعراض الاكتئاب.
- **Related Concepts:** KB-136, KB-138
- **Potential Visual:** دوامة (اجترار) تتحول إلى سلم صغير (خطوة صغيرة).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE] + [SAFETY]
- **CT#:** 156, 132

### KB-051 · الافتراضات الضمنية «إذا… إذن…» والتجارب السلوكية | Underlying Assumptions & Behavioral Experiments
- **Definition:** الافتراضات «the rules we live by»، تُصاغ «If… then…»؛ «It is impossible to know what people's underlying assumptions are just by looking at their behaviors». تُختبر بـ**تجارب سلوكية**: (1) هل «then» تتبع «If» دائمًا؟ (2) راقب الآخرين (3) افعل العكس؛ «Problem Solve, Don't Quit»؛ و«at least three behavioral experiments before drawing a conclusion». نتعلمها من الأسرة والثقافة، «because assumptions are learned, we can learn new assumptions».
- **Book:** MoM
- **Chapter:** Ch.11
- **Page:** p.132–150
- **Example:** ★ شونتيل وتري: «If we don't arrive on time, then it will be disrespectful» مقابل «If we arrive on time, then it will pressure the hosts» ← «their conflicting assumptions guaranteed tension» (p.132–133).
- **Application:** يفسر كثيرًا من خلافات CASE 2 (زوجين) وCASE 3 (مقاول ومدير مشروع): قواعد خفية مختلفة لا «شر». وافتراضات إرضاء الآخرين («People won't like me if I say no») تُستخدم في المرحلة 7.
- **Related Concepts:** KB-052, KB-066, KB-079, KB-111
- **Potential Visual:** كتابا قواعد مختلفان في يد كل طرف، بنفس الغلاف وعناوين داخلية متعاكسة.
- **Potential Exercise:** «كمّل الجملة: لو قلت لأ… يبقى…» — ثم «جرّب مرة صغيرة وشوف حصل إيه».
- **Tag:** [DIRECT SOURCE]
- **CT#:** 123, 125

### KB-052 · المعتقدات الجوهرية والسهم الهابط | Core Beliefs & Downward Arrow
- **Definition:** «Core beliefs are all-or-nothing statements about yourself, others, or the world»؛ «Everybody has both negative and positive core beliefs. This is normal». ثلاث طبقات: أفكار تلقائية ← افتراضات ← معتقدات جوهرية (استعارة الحديقة: الأعشاب فوق الأرض والجذور تحتها). **السهم الهابط**: «If this is true, what does this mean about me?». المعتقدات تُزرع في الطفولة: «They teach us things like "The sky is blue. This is a dog. You are worthless."… we believe all the things we are told, even things that may be wrong». لا نحتاج التخلص من المعتقد السلبي بل بناء معتقد جديد وجمع أدلته؛ «Confidence in a new core belief usually takes months».
- **Book:** MoM
- **Chapter:** Ch.12
- **Page:** p.152–169
- **Example:** «I don't think Marsha likes me» ← «I'm unlikable» (السهم الهابط، p.156–157). استعارة الوعاء المثقوب: بدون معتقد إيجابي، التجارب الإيجابية «drains away» (p.164).
- **Application:** طبقة عمق اختيارية (دقيقة واحدة في الحلقة) — تُستخدم أساسًا لفهم لماذا يستجيب البعض للتلاعب بالذنب («أنا شخص سيئ» في مثال الـBrief) — انظر KB-103.
- **Related Concepts:** KB-051, KB-103, KB-114
- **Potential Visual:** شجرة: الأوراق = أفكار تلقائية، الجذع = افتراضات، الجذور = معتقدات.
- **Potential Exercise:** — (يُذكر كقراءة إضافية)
- **Tag:** [DIRECT SOURCE]
- **CT#:** 126

### KB-053 · الغضب جرس إنذار — وتحته احتياج | Anger as Wake-Up Call; the Need Beneath
- **Definition:** NVC: «all anger has a life-serving core»؛ «Use anger as a wake-up call». **أربع خطوات للتعبير عن الغضب**: (1) Stop. Breathe (2) حدد الأفكار الحُكمية (3) اتصل باحتياجاتك (4) عبّر عن مشاعرك واحتياجاتك غير الملباة. و«Stay conscious of the violent thoughts that arise in our minds, without judging them». KZ (Cat-Food Lessons): راقب غضبه دون فعل: اشمئزاز (1–2 ثانية) ← إحساس بالخيانة ← «it's not really the cat food… It's that I'm not feeling listened to and respected». Goleman: ردود الأفعال «تمس بعض احتياجاتنا الدفينة… أن نكون محبوبين وموضع احترام أو خوفنا من الهجر» (ص207).
- **Book:** NVC · KZ · Goleman
- **Chapter:** NVC Ch.10؛ KZ «Cat-Food Lessons»؛ Goleman ف9
- **Page:** NVC L2758–2864؛ KZ PDF p.159–160؛ Goleman ص207
- **Example:** NVC: سام ويليامز وبطاقة 3×5 — «Daddy, get the card!» (L2906–2916).
- **Application:** يربط المرحلة 3 بالمرحلة 4–5: تحت الشعور احتياج؛ وتحت الغضب غالبًا «احترام/تقدير/أمان». أساس CASE 2 (أطباق المطبخ ≈ طعام القطط).
- **Related Concepts:** KB-027, KB-063, KB-072, KB-116
- **Potential Visual:** جبل جليد: القمة «غضب»، تحت الماء «مجروح ← مش متشاف ← محتاج احترام».
- **Potential Exercise:** «تحت غضبك آخر مرة… كنت محتاج إيه؟» (اختيار من قائمة احتياجات مختصرة).
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 66, 99

### KB-054 · القبول ليس استسلامًا | Acceptance ≠ Resignation
- **Definition:** KZ: «acceptance of the present moment has nothing to do with resignation… Acceptance doesn't tell you what to do. What happens next, what you choose to do, that has to come out of your understanding of this moment». MoM: «acceptance does not mean that we need to think positively about negative events or feel happy… Acceptance means that we acknowledge the difficulties… and figure out how to live with them in ways consistent with our values»؛ «Acceptance of your thoughts should not be confused with believing that your thoughts are accurate»؛ ثلاث طرق: المراقبة دون حكم، الصورة الكبيرة، القيم. متى نستخدم ماذا: تقوية الأفكار، خطة العمل (مشكلة حقيقية)، القبول (ما لا يُحل).
- **Book:** KZ · MoM
- **Chapter:** KZ «This Is It»؛ MoM Ch.10
- **Page:** KZ PDF p.23؛ MoM p.127–131
- **Example:** MoM: رودني يزور أباه المصاب بالخرف: «My name is Rodney. I like to come here and talk to people…» (p.127–128).
- **Application:** يحمي الحلقة من سوء فهم «اقبل كل حاجة»؛ وهو الأساس المصدري لجملة الـBrief **«الهدوء ليس استسلامًا»** [USER-PROVIDED FRAMEWORK مدعوم بـKZ + MoM].
- **Related Concepts:** KB-022, KB-028, KB-115, KB-122
- **Potential Visual:** يدان: واحدة مفتوحة تستقبل (قبول)، وأخرى مرفوعة بعلامة «قف» (فعل) — في الإطار نفسه.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ الربط بجملة الـBrief = [INTEGRATED SYNTHESIS]
- **CT#:** 75, 122

### KB-055 · التفاؤل أسلوب تفسير — والأمل مهارة | Optimism as Explanatory Style; Hope
- **Definition:** سليجمان: المتفائل يُرجع الفشل لشيء يمكن تغييره، والمتشائم لصفة دائمة فيه؛ المطلوب «التفاؤل الواقعي»، و«التفاؤل المفرط في السذاجة قد يسبب الكوارث». الحوار الداخلي: «أنا فاشل… لن أستطيع أن أبيع شيئًا» مقابل «قد أكون دخلت من المدخل الخطأ… الشخص كان في حالة نفسية سيئة». سنايدر: الأمل «اعتقادك بأنك تملك الإرادة والوسيلة لتحقيق أهدافك» + تقسيم المهمة الصعبة. «من الممكن تعلم التفاؤل والأمل، مثل تعلم العجز واليأس».
- **Book:** Goleman
- **Chapter:** ف6 «القدرة المسيطرة»
- **Page:** ص128–133
- **Example:** السباح مات بيوندي في أولمبياد 1988 — أداؤه بعد تغذية راجعة سلبية مصطنعة (ص130–131) [REPORTED IN SOURCE].
- **Application:** يوسّع REFRAME من «موقف» إلى «أسلوب»؛ ويدعم يوم REFLECT (كيف تفسر نكساتك في خطة الأيام السبعة).
- **Related Concepts:** KB-045, KB-133, KB-136
- **Potential Visual:** نفس الحدث (باب مقفول) — لافتة «أنا فاشل (دائم)» مقابل «الباب ده مقفول النهارده (مؤقت)».
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]
- **CT#:** 159

### KB-056 · التعاطف مع الذات — من «ينبغي» إلى الحداد والمسامحة | Self-Empathy, Mourning, Self-Forgiveness
- **Definition:** NVC: «When we are internally violent toward ourselves, it is difficult to be genuinely compassionate toward others»؛ «Avoid shoulding yourself!»؛ الأحكام الذاتية تعبير مأساوي عن احتياجات غير ملباة ⇒ **الحداد** (الاتصال بالاحتياج الذي لم يُلبَّ) ثم **المسامحة الذاتية** (ما الاحتياج الذي كنت أحاول تلبيته؟). MoM: «Being a good person doesn't mean that you will never do bad things»؛ «I made this mistake because I'm an awful person» ← «I made this mistake during an awful time in my life»؛ «view yourself with the same kindness or compassion with which you view others».
- **Book:** NVC · MoM
- **Chapter:** NVC Ch.9؛ MoM Ch.15
- **Page:** NVC L2554–2616؛ MoM p.277–278
- **Example:** NVC: بدلة البولكا المنقطة — 20 دقيقة من جلد الذات تنتهي باحتياج «أن أعتني بنفسي» (L2620–2634).
- **Application:** يُعادل حدة أدوات REFRAME: الهدف ليس محاكمة النفس. يدعم الختام ويوم REFLECT.
- **Related Concepts:** KB-044, KB-119, KB-081
- **Potential Visual:** صوتان داخليان: «قاضٍ» يطرق بالمطرقة ↔ «صديق» يضع يده على الكتف.
- **Potential Exercise:** «اكتب اللي بتقوله لنفسك لما تغلط… وبعدين اكتبه بصوت صاحبك».
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 64

### KB-057 · التحيز العدائي وشخصنة الأفعال | Hostile Attribution & Personalizing
- **Definition:** Goleman: الأطفال العدوانيون يشعرون «بالإهانة التي لم يقصدها أحد» ويؤولون الاصطدام البريء «ثأرًا مقصودًا» و«يتصورون دائمًا سوء النية بدلًا من حسن النية» (ص322–324)؛ والأزواج العنيفون يتصورون «نية عدائية حتى في تصرفاتهن المحايدة» (ص199–200). برنامج لوكمان: إعادة تفسير المواقف، منظور الآخر، رصد إشارات الجسد (ص326–328). MoM: «When we get angry, we tend to personalize other people's actions»؛ «Can you remember a time when you stepped in front of someone else… because you didn't see that person?»؛ **«وضع الناس في صناديق»** (careless/thoughtless) يجعل كل سلوك دليلًا؛ الحل: «be a nonjudgmental observer and get more information» (p.258–259).
- **Book:** Goleman · MoM
- **Chapter:** Goleman ف9، ف15؛ MoM Ch.15
- **Page:** Goleman ص199–200، ص322–328؛ MoM p.257–259
- **Example:** MoM: الطفل الذي داس قدمك في الأتوبيس — الأتوبيس المزدحم مقابل الفارغ (p.257–258) — يصلح مباشرة لـ«المترو الزحمة».
- **Application:** CASE 4 (واتساب) وCASE 1. **وتحذير مركزي في Dark EQ**: نفس آلية «الصندوق» تجعلنا نلصق «متلاعب» بشخص من موقف واحد ⇒ ONE INCIDENT vs REPEATED PATTERN (KB-094).
- **Related Concepts:** KB-038, KB-047, KB-094, KB-114
- **Potential Visual:** شخص يُوضع داخل صندوق مكتوب عليه «أناني»؛ كل فعل جديد يطير ويسقط في الصندوق تلقائيًا.
- **Potential Exercise:** «افتكر مرة انت اللي عملت حاجة من غير قصد وحد فهمها غلط».
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]؛ المصطلح «hostile attribution bias» = [EXTERNAL KNOWLEDGE] (لدودج؛ Goleman يصف الظاهرة دون المصطلح)
- **CT#:** 184, 137

---

# المرحلة 4 — EMPATHIZE | تعاطف
*العمود الفقري: Goleman ف7 «جذور التعاطف» + ف8 «الفنون الاجتماعية». الأداة الرئيسية: NVC ف7–8. داعم: CC ف8 + MoM.*

### KB-058 · التعاطف يقوم على الوعي بالذات | Empathy Builds on Self-Awareness
- **Definition:** «ويقوم التعاطف على أساس الوعي الذاتي. فبقدر ما نكون قادرين على تقبل مشاعرنا وإدراكها نكون قادرين على قراءة مشاعر الآخرين». الفشل في تسجيل مشاعر الآخر «أكبر نقطة ضعف في الذكاء العاطفي»؛ والتعاطف مستقل عن IQ و«شعور يمكن تعلمه».
- **Book:** Goleman
- **Chapter:** ف7
- **Page:** ص143–145
- **Example:** جاري الجراح الألكسيثيمي ينتقد خطيبته «معتقدًا أنه يساعدها»، ولا يدرك أنها تسمعه هجومًا (ص143).
- **Application:** **المبرر المصدري لترتيب المراحل**: NOTICE/NAME قبل EMPATHIZE. جملة انتقالية: «مش هتعرف تقرا غيرك… قبل ما تعرف تقرا نفسك».
- **Related Concepts:** KB-018, KB-035, KB-060
- **Potential Visual:** مرآة تتحول إلى نافذة.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]
- **CT#:** 160

### KB-059 · الحقيقة في «الكيف» لا في «الكلام» | Emotional Truth Lives in the How
- **Definition:** «عواطف البشر من النادر أن تتجسد في كلمات… تُترجم… من خلال إيماءات وتلميحات»؛ «عندما لا تتفق كلمات شخص مع… نغمة صوته أو إيماءته… تظهر حقيقة عواطفه في الكيفية التي يقول بها شيئًا ما أكثر من الشيء نفسه». CC (Mirror): «You say you're okay, but by the tone of your voice, you seem upset» — النبرة أهم عنصر. KZ: طلاب الطب يسألون «Is there anything else you would like to tell me?» وهم يهزون رؤوسهم «No, please, don't tell me any more!».
- **Book:** Goleman · CC · KZ
- **Chapter:** Goleman ف7؛ CC Ch.8؛ KZ «Is There Anything Else You Would Like to Tell Me?»
- **Page:** Goleman ص144–146؛ CC p.149–150؛ KZ PDF p.122–123
- **Example:** اختبار PONS (روزنتال): قارئو الإشارات غير اللفظية أفضل تكيفًا وأكثر محبوبية (ص144–145) [REPORTED IN SOURCE].
- **Application:** مهارة قراءة الآخر في المرحلة 4؛ ثم في Dark EQ كأساس لبند **«الأفعال قبل الكلمات»** — مع تحذير: التناقض إشارة للسؤال، لا دليل لقراءة الأفكار.
- **Related Concepts:** KB-062, KB-025, KB-101
- **Potential Visual:** ترجمة مزدوجة أسفل الشاشة: «الكلام: أنا تمام» / «النبرة والجسم: أنا مش تمام».
- **Potential Exercise:** مشهد صامت 5 ثوانٍ (ممثل) والمشاهد يخمّن الشعور قبل سماع الجملة.
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 161, 91

### KB-060 · التعاطف يحتاج هدوءًا | Empathy Requires Calm
- **Definition:** ليفنسون: التعاطف الأدق عند من توافقت ردودهم الفسيولوجية؛ و«عندما يدفع [المخ العاطفي] الجسم إلى رد فعل شديد، مثل حرارة الغضب… قد يتوافر… قدر قليل من التعاطف… أو لا يوجد على الإطلاق. فالتعاطف يتطلب قدرًا كافيًا من الهدوء والاستقبالية». NVC: «We need empathy to give empathy»: (1) توقف، تنفّس، أعطِ نفسك تعاطفًا (2) «scream nonviolently» (3) خذ وقتًا مستقطعًا. Goleman ص167: «التوافق مع الآخرين يتطلب قليلًا من الهدوء النفسي».
- **Book:** Goleman · NVC
- **Chapter:** Goleman ف7، ف8؛ NVC Ch.7
- **Page:** Goleman ص154–155، ص167؛ NVC L2177–2199
- **Example:** NVC: روزنبرج في التاكسي بعد تعليق عنصري: أنفاس عميقة، تعاطف مع الذات، ترك الأفكار العنيفة تمر، ثم تعاطف 10 دقائق، ثم عبّر عن ألمه (L2852–2902).
- **Application:** **المبرر المصدري لوضع REGULATE قبل EMPATHIZE** في الإطار النهائي. يفسر لماذا «حاول تفهمه» لا تنجح وأنت في الذروة.
- **Related Concepts:** KB-058, KB-022, KB-092
- **Potential Visual:** جهاز استقبال راديو: التشويش (غضب) يمنع الإشارة (مشاعر الآخر) حتى يُضبط.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 163, 61

### KB-061 · التعاطف حضور — وعوائقه العشرة | Empathy as Presence; Blocks to Empathy
- **Definition:** «Empathy is a respectful understanding of what others are experiencing»؛ «Empathy lies in our ability to be present». عوائق التعاطف (عن هولي همفري): النصيحة، المزايدة، التعليم، المواساة، الحكي عن نفسك، الإغلاق، الشفقة، الاستجواب، الشرح، التصحيح. «Intellectual understanding blocks empathy»؛ التعاطف ≠ الشفقة. «Listen to what people are needing rather than what they are thinking». Goleman يفرّق بالمثل بين Empathy وSympathy (تيتشنر، ص146–148).
- **Book:** NVC · Goleman
- **Chapter:** NVC Ch.7–8؛ Goleman ف7
- **Page:** NVC L1987–2075، L2544؛ Goleman ص146–148
- **Example:** NVC: «I don't want you to do anything; I just want you to listen» (L2349–2357)؛ ابنة تقول «أنا وحشة زي…» فتُقابَل بالطمأنة بدل التعاطف (L1999–2001).
- **Application:** **Exercise 5: Empathy** — المشاهد يتعرف على «عائقه المفضل». قصة مصرية: صاحبك بيحكي مشكلة وانت بترد بـ«ولا يهمك… أنا حصل لي أسوأ».
- **Related Concepts:** KB-062, KB-063, KB-022
- **Potential Visual:** 10 أيقونات عوائق (ميكروفون، إصبع، كتاب…) تسقط واحدة واحدة حتى يبقى «ودن».
- **Potential Exercise:** **Exercise 5**: جملة من صديق + 4 ردود؛ المشاهد يختار الرد المتعاطف ويسمّي عائق الباقي.
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 59

### KB-062 · التوافق وإعادة الصياغة كسؤال | Attunement & Paraphrasing as a Question
- **Definition:** Goleman (دانييل ستيرن): **التوافق** ≠ التقليد: «إذا قلدت طفلًا… تظهر له أنك تعرف ماذا فعل… أما إذا أردت أن تجعله يعرف أنك تشعر… تسترجع مشاعره الداخلية بطريقة أخرى». الاستماع غير الدفاعي: حذف الأجزاء العدائية وسماع «الرسالة الأساسية»، و«التعاطف… هو في الحقيقة استماع إلى المشاعر التي تغلفها الكلمات»، ثم «الانعكاس» (Mirroring) مع التحقق. NVC: إعادة الصياغة **بصيغة سؤال** («Are you unhappy because you are needing…?») لا ادعاء؛ النبرة «asking not claiming». CC: Paraphrase بكلماتك مختصرًا وبهدوء.
- **Book:** Goleman · NVC · CC
- **Chapter:** Goleman ف7، ف9؛ NVC Ch.7؛ CC Ch.8
- **Page:** Goleman ص148–151، ص209–211؛ NVC L2047–2131؛ CC p.150–151
- **Example:** Goleman: «أنت تصرخ» / «طبعًا أنا أصرخ لأنك لا تنصت» ← البديل: «أوكي، استمري…» (ص209–210).
- **Application:** صيغة ثابتة للحلقة: «يعني انت حاسس بـ… عشان محتاج… صح؟» — في CASE 1 وCASE 2.
- **Related Concepts:** KB-061, KB-090, KB-072
- **Potential Visual:** موجتا صوت تتزامنان تدريجيًا (توافق) بدل نسخ متطابق (تقليد).
- **Potential Exercise:** «أعد صياغة الجملة دي كسؤال»: 3 جمل غاضبة.
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 162, 60, 173

### KB-063 · الأحكام تعبير مغترب عن احتياجات — وقائمة الاحتياجات | Judgments as Alienated Needs; Needs List
- **Definition:** «Judgments of others are alienated expressions of our own unmet needs»؛ «analyses of other human beings are tragic expressions of our own values and needs». «You love your work more than you love me» = احتياج للقرب. قائمة الاحتياجات: الاستقلالية، الاحتفاء، النزاهة، الترابط (قبول، تقدير، قرب، احترام، أمان عاطفي، ثقة…)، اللعب، الاتصال الروحي، الرعاية الجسدية. «from the moment people talk about needs rather than what's wrong with one another, possibility increases». Goleman: ردود الأفعال تمس «احتياجاتنا الدفينة… أن نكون محبوبين وموضع احترام» (ص207).
- **Book:** NVC · Goleman
- **Chapter:** NVC Ch.2، Ch.5؛ Goleman ف9
- **Page:** NVC L638–640، L1215–1409؛ Goleman ص207
- **Example:** NVC: المختار الذي ينادي روزنبرج «نازي» ← ترجمة الإهانة لاحتياجات (L1225–1231).
- **Application:** «مترجم الإهانات»: كل اتهام يُترجم لاحتياج. يُستخدم في CASE 2 وCASE 3 وفي Exercise 5.
- **Related Concepts:** KB-053, KB-072, KB-096
- **Potential Visual:** «مترجم» — سماعة تحوّل «انت أناني» إلى «أنا محتاج اهتمام».
- **Potential Exercise:** «ترجم الشتيمة»: 4 جمل اتهام ← الاحتياج وراء كل واحدة.
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 53, 54

### KB-064 · الفضول وقت الغضب | Curiosity at the Moment of Fury
- **Definition:** «at the very moment when most people become furious, we need to become curious»؛ السؤال: «Why would a reasonable, rational, and decent person say this?». الصبر لأن كيمياء الانفعال «hang around in the bloodstream for a time—in some cases, long after thoughts have changed». «Every sentence has a history». اعتبر الصمت والعنف علامات أن الآخر لا يشعر بالأمان — «be curious, not angry or frightened».
- **Book:** CC
- **Chapter:** Ch.4، Ch.6، Ch.8
- **Page:** p.50–51، p.112–114، p.143–147
- **Example:** Goleman يقدم نسخة عملية: المهندس يسأل نائب الرئيس المتهكم: «وأنا أفترض أنك لم تقصد مجرد إحراجي، فهل كان لديك أهداف أخرى…؟» (ص216–217).
- **Application:** CASE 1 (نقد أمام الفريق). **[BOOK DIFFERENCE ناعم]**: CC يفترض أن الهجوم علامة عدم أمان عند الآخر؛ Dark EQ يضيف أن التكرار قد يكون تكتيكًا ⇒ الفضول أولًا، ثم النمط يحدد (KB-094). CC نفسه: الأنسنة «is not to excuse others» (p.114).
- **Related Concepts:** KB-047, KB-077, KB-094
- **Potential Visual:** علامة تعجب حمراء (!) تتحول إلى علامة استفهام زرقاء (؟).
- **Potential Exercise:** «ليه شخص عاقل ومحترم ممكن يقول الكلام ده؟» — 3 احتمالات.
- **Tag:** [DIRECT SOURCE]؛ الربط بـGoleman = [INTEGRATED SYNTHESIS]
- **CT#:** 29

### KB-065 · الفهم ليس موافقة | Understanding ≠ Agreement
- **Definition:** CC: «Understanding doesn't equate with agreement». Goleman (نصيحة جوتمان للأزواج): الأهم «استماع… وتعاطفه مع مشاعرها… على الرغم من عدم اتفاقه معها» (ص204)، والاعتراف بوجاهة منظور الآخر «حتى لو كنت… لا توافق» (ص210).
- **Book:** CC · Goleman
- **Chapter:** CC Ch.8؛ Goleman ف9
- **Page:** CC p.153؛ Goleman ص204، ص210
- **Example:** —
- **Application:** يفك عقدة «لو اتعاطفت معاه يبقى وافقته». **ركيزة في Dark EQ**: «أفهمك» لا تعني «هنفذ» — التعاطف مع شخص يضغطك ≠ الامتثال له.
- **Related Concepts:** KB-062, KB-074, KB-124
- **Potential Visual:** رأسان متقابلان: خط «فهم» يصل بينهما، بينما لافتة «موافقة؟» تبقى مفتوحة بعلامة استفهام.
- **Potential Exercise:** «قول جملة تفهُّم من غير ما توافق»: «أنا فاهم إنك متضايق من…، وأنا شايف الموضوع بشكل مختلف».
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 31

### KB-066 · معلومة صغيرة تقلب الصورة | A Little Information Shifts It 180°
- **Definition:** «Sometimes a little bit of additional information shifts our interpretation and understanding of a situation 180 degrees». Goleman: المعلومة المخففة («كان تحت ضغط الامتحانات») تهدئ الغضب المتوسط (ص94–95).
- **Book:** MoM · Goleman
- **Chapter:** MoM Ch.9؛ Goleman ف5
- **Page:** MoM p.95؛ Goleman ص94–95
- **Example:** ★ أكيكو ترى فوضى المطبخ فتغضب: «Yuki is so inconsiderate»، ثم تجد بطاقة: «I love you, Mom! Please get well soon!» (MoM p.95). وفيك يكتشف أن تعبير جودي كان لأنها تذكرت عيد ميلاد أختها — «she hadn't been thinking about Vic at all!» (p.96–98).
- **Application:** قصة افتتاح المرحلة 4 (قابلة للتمصير: الأم والمطبخ والكارت). تُعلّم عادة «اسأل قبل ما تحكم».
- **Related Concepts:** KB-038, KB-043, KB-064
- **Potential Visual:** كاميرا تعمل Zoom-out تدريجيًا: المطبخ المبعثر ← كارت على الترابيزة.
- **Potential Exercise:** «افتكر مرة غيّرت رأيك في حد بعد ما عرفت معلومة واحدة».
- **Tag:** [DIRECT SOURCE]
- **CT#:** 118

### KB-067 · أربع خيارات لتلقي رسالة سلبية | Four Options for Receiving a Negative Message
- **Definition:** عندما يصلك كلام سلبي: (1) لُم نفسك (2) لُم الآخر (3) انتبه لمشاعرك واحتياجاتك (4) انتبه لمشاعر الآخر واحتياجاته. KZ: «We might begin by taking things a little less personally… Maybe it's not aimed at you». Goleman (للمتلقي): انظر للنقد كمعلومة لا هجوم، وراقب «حافزك إلى… موقف دفاعي»، واطلب اجتماعًا لاحقًا بعد الهدوء (ص220–221).
- **Book:** NVC · KZ · Goleman
- **Chapter:** NVC Ch.5؛ KZ «Selfing»؛ Goleman ف10
- **Page:** NVC L1153–1167؛ KZ PDF p.155–157؛ Goleman ص220–221
- **Example:** NVC: «The Most Arrogant Speaker» — ثلاثة اختيارات: خذها شخصيًا، هاجم، أو ركّز على ما وراء الكلام (L877–901).
- **Application:** الأداة الأساسية في **CASE 1** (مدير ينتقد موظفًا أمام الفريق): 4 أبواب على الشاشة ونختار الثالث ثم الرابع.
- **Related Concepts:** KB-062, KB-077, KB-057
- **Potential Visual:** 4 أبواب (لوم النفس — لوم الآخر — مشاعري/احتياجي — مشاعره/احتياجه).
- **Potential Exercise:** «أنهي باب بتفتحه أوتوماتيك؟»
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 51, 97

### KB-068 · الجودو العاطفي | Emotional Aikido
- **Definition:** «التعامل مع من يكون في ذروة غضبه… أعلى مقياس» للمهارة الاجتماعية: صرف نظر الغاضب عن موضوع غضبه + التعاطف مع مشاعره + جذبه لمركز اهتمام بديل بمشاعر إيجابية.
- **Book:** Goleman
- **Chapter:** ف8
- **Page:** ص182–185
- **Example:** ★ قطار طوكيو (تيري روبنسون): سكير عنيف؛ عجوز ياباني يقول «هيه!» بمرح، يسأله ماذا كان يشرب، يحكي عن الساكي وشجرة البرسيمون — فينهار السكير باكيًا ورأسه في حجر العجوز.
- **Application:** قصة محورية لمرحلة EMPATHIZE أو NAVIGATE. **[SAFETY + BOOK DIFFERENCE D4]**: تُقدَّم كمثال على قوة التعاطف **لا كتعليمة** بمواجهة شخص عنيف؛ مع الشخص الخطر الأولوية للحماية (MoM p.263؛ NVC Ch.12).
- **Related Concepts:** KB-060, KB-069, KB-117, KB-118
- **Potential Visual:** رسم متحرك بأسلوب الحبر لمشهد القطار (بدون عنف مصور).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] (قصة ينقلها Goleman) + [SAFETY]
- **CT#:** 169

### KB-069 · العدوى العاطفية | Emotional Contagion
- **Definition:** «نحن ننقل المشاعر لبعضنا البعض كما لو أنها فيروسات اجتماعية»؛ الحالة تنتقل من الأكثر تعبيرًا إلى الأكثر سلبية؛ التناسق الحركي = ألفة. MoM (أفعال الطيبة): ابتسام بادسكي في مكتب البريد لأسابيع ← «the post office became a place of good humor» — «Acts of kindness… can help transform the places we go».
- **Book:** Goleman · MoM
- **Chapter:** Goleman مقدمة، ف8؛ MoM Ch.12
- **Page:** Goleman ص7، ص168–172؛ MoM p.184–185
- **Example:** الرهبان الفيتناميون الستة عبروا خط النار فانطفأت رغبة الجنود في القتال (ص168). سائق حافلة نيويورك (ص7).
- **Application:** الوجه الإيجابي للعدوى في المرحلة 5–8؛ والوجه المظلم (من يضبط «إيقاع» الجماعة) في KB-102.
- **Related Concepts:** KB-102, KB-080, KB-129
- **Potential Visual:** موجة لون تنتشر في غرفة من شخص واحد.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]
- **CT#:** 167, 130

### KB-070 · التعاطف مع الأقوى أصعب — والتعاطف مع «لا» | Empathy Upward; Empathy for "No"
- **Definition:** «It's harder to empathize with those who appear to possess more power, status, or resources»؛ ومن يريد «tough image» يتجنب إظهار الضعف خوفًا على سلطته. التعاطف مع «لا» الآخر يحمينا من أخذها بشكل شخصي — «لا» تخفي احتياجًا يمنع «نعم» (L3232–3234).
- **Book:** NVC
- **Chapter:** Ch.8، Ch.11
- **Page:** L2361–2371، L2464–2480، L3232–3234
- **Example:** أعضاء هيئة التدريس تعاطفوا مع العميد فتغير الحوار (L2361–2367).
- **Application:** CASE 1 (المدير) وCASE 3 (مدير المشروع): «المدير برضه إنسان عنده خوف». ويُذكر في Dark EQ بحدود: التعاطف مع صاحب السلطة لا يعني قبول الإساءة.
- **Related Concepts:** KB-064, KB-107
- **Potential Visual:** سلم هرمي — سهم تعاطف يصعد لأعلى بصعوبة.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]
- **CT#:** 62, 63

### KB-071 · التدريب العاطفي في الأسرة | Emotion Coaching (Parenting Styles)
- **Definition:** «الأسرة هي المدرسة الأولى للتعلم العاطفي». ثلاثة أساليب أبوية سيئة: تجاهل المشاعر؛ «دعه وشأنه» والرشوة للتخلص من الانفعال؛ احتقار مشاعر الطفل («اسكت تمامًا، لا ترد عليّ»). الأسلوب الرابع — **المدرب العاطفي**: «هل أنت غاضب لأن تومي جرح مشاعرك؟» + بديل إيجابي. وتربية تقول «انظر كيف جعلتها تشعر بالحزن» بدل «كان سلوكك هذا شقاوة» تنمّي التعاطف (ص147–148). KZ: «advice is probably the last thing that will be useful» مع الأبناء.
- **Book:** Goleman · KZ
- **Chapter:** Goleman ف7، ف12؛ KZ «Parenting as Practice»
- **Page:** Goleman ص147–148، ص265–268؛ KZ PDF p.161–166
- **Example:** كارل وآن وابنتهما ليسلي ولعبة الفيديو: أوامر متضاربة وتجاهل دموعها (ص265–266).
- **Application:** يُوسّع الحلقة إلى «التعامل مع الأسرة» (مطلب الجمهور). مثال مصري: «بطّل عياط، راجل ما بيعيطش» ← البديل المتعاطف.
- **Related Concepts:** KB-062, KB-109, KB-061
- **Potential Visual:** طفل وأب — ثلاث فقاعات رد مشطوبة، ثم فقاعة «انت زعلان عشان…؟».
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]
- **CT#:** 180

---

# المرحلة 5 — COMMUNICATE | تواصل
*العمود الفقري: Goleman ف9 «الأعداء الحميمون» + ف10 «التحكم بالعاطفة/الإدارة بالقلب». الأداة الرئيسية: NVC. داعم: MoM ف15 (التوكيد).*

### KB-072 · مكونات NVC الأربعة | The Four Components of NVC
- **Definition:** **ملاحظة** (ما أراه/أسمعه دون تقييم) + **شعور** + **احتياج** + **طلب** (فعل محدد يثري الحياة). جزءان: التعبير بصدق، والاستقبال بتعاطف. «NVC is not a set formula»؛ جوهرها الوعي بالمكونات الأربعة.
- **Book:** NVC
- **Chapter:** Ch.1 «Giving From the Heart»
- **Page:** L474–512
- **Example:** مثال الجوارب (L486–488): «Felix, when I see two balls of soiled socks under the coffee table… I feel irritated because I am needing more order… Would you be willing to put your socks in your room or in the washing machine?» (صياغة الكتاب). نموذج مكتمل في مثال بنك الطعام (L1535).
- **Application:** Animation 6 «NVC Model» و**Exercise 6: NVC Sentence**. القالب المصري: «لما … (شفت/سمعت)، حسيت بـ…، عشان كنت محتاج …، ممكن …؟».
- **Related Concepts:** KB-043, KB-035, KB-063, KB-074, KB-075
- **Potential Visual:** 4 قطع بازل تتجمع: عين (ملاحظة) — قلب (شعور) — جذر (احتياج) — يد ممدودة (طلب).
- **Potential Exercise:** **Exercise 6**: حوّل «انت دايمًا بتتأخر ومش فارق معاك» إلى جملة NVC كاملة.
- **Tag:** [DIRECT SOURCE]
- **CT#:** 44

### KB-073 · التواصل المُغرِّب عن الحياة | Life-Alienating Communication
- **Definition:** أشكال تعطل الرحمة: **الأحكام الأخلاقية** («Blame, insults, put-downs, labels, criticism, comparisons, and diagnoses are all forms of judgment»)، **المقارنات**، **إنكار المسؤولية** («have to»، «makes me feel»، «أوامر الرؤساء»، ضغط الجماعة، السياسات، الأدوار)، **المطالبات** (تهديد باللوم/العقاب — شائعة «among those who hold positions of authority»)، وتفكير «يستحق». الامتثال خوفًا أو ذنبًا أو خجلًا ← استياء وتراجع تقدير الذات. «We can never make people do anything».
- **Book:** NVC
- **Chapter:** Ch.2 «Communication That Blocks Compassion»
- **Page:** L618–746
- **Example:** أيخمان و«Amtssprache» — «لغة المكاتب» التي تنفي المسؤولية (L690–700).
- **Application:** قائمة «ممنوعات» المرحلة 5، وتمهيد لإنكار المسؤولية ولغة السلطة في Dark EQ (KB-106).
- **Related Concepts:** KB-074, KB-106, KB-128
- **Potential Visual:** جدار من الطوب؛ كل طوبة مكتوب عليها نوع (حكم، مقارنة، «لازم»، «هو اللي خلاني») تمنع وصول الصوت.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]
- **CT#:** 45, 46

### KB-074 · الطلب مقابل المطالبة | Requests vs. Demands
- **Definition:** المطالبة تجعل الآخر أمام خيارين: الخضوع أو التمرد. **الاختبار**: ماذا يفعل المتكلم إن لم يُستجب له؟ إن انتقد أو حكم أو **ألقى بالذنب** ⇒ كانت مطالبة؛ إن تعاطف ⇒ كانت طلبًا. مثال الكتاب: «If you really loved me, you'd spend the evening with me». الطلب لا يعني الاستسلام بعد «لا»، لكن لا إقناع قبل التعاطف. **«If our objective is only to change people and their behavior or to get our way, then NVC is not an appropriate tool.»**
- **Book:** NVC
- **Chapter:** Ch.6
- **Page:** L1761–1801
- **Example:** جاك وجين (L1761–1797).
- **Application:** أداة مزدوجة: في المرحلة 5 لتحسين طلباتي؛ **وفي المرحلة 7 كأداة كشف مباشرة**: جملة الـBrief «لو كنت بتحترمني كنت وافقت» تطابق بنية مثال NVC ⇒ مطالبة مغلفة بالذنب. وجملة «if our objective is… to get our way» = الحد الأخلاقي لاستخدام أدوات الذكاء العاطفي.
- **Related Concepts:** KB-072, KB-103, KB-118, KB-124
- **Potential Visual:** طريقان بعد «لا»: (أ) تعاطف ← طلب؛ (ب) لوم/ذنب ← مطالبة.
- **Potential Exercise:** جزء من **Exercise 8: Dark EQ Detection**: «طلب ولا مطالبة؟» — 5 جمل.
- **Tag:** [DIRECT SOURCE]
- **CT#:** 57, 58

### KB-075 · لغة الفعل الإيجابي والطلب المحدد | Positive, Concrete Action Language
- **Definition:** اطلب ما **تريده** لا ما لا تريده («How do you do a don't?»)، وبأفعال محددة قابلة للتنفيذ لا بعبارات مبهمة («let me be me»). «Often, the use of vague and abstract language can mask oppressive interpersonal games». «whenever we say something to another person, we are requesting something in return». MoM (استراتيجية توكيد 3): «Make clear and simple statements of your wants and needs, rather than expecting other people to read your mind».
- **Book:** NVC · MoM
- **Chapter:** NVC Ch.6؛ MoM Ch.15
- **Page:** NVC L1595–1693؛ MoM p.262
- **Example:** الزوجة التي طلبت من زوجها «ألا يقضي وقتًا طويلًا في العمل» فاشترك في بطولة جولف (L1597–1601). قطار المطار: «I have never seen a train go so slow» — طلب غير واضح (L1669–1693).
- **Application:** CASE 4 (رسالة واتساب غامضة): الرسالة الغامضة تستدعي التفسير السلبي؛ الطلب الواضح يقطع الطريق. وفي CASE 3: «عايز التسليم الخميس الساعة 2» بدل «خلّصوا بسرعة».
- **Related Concepts:** KB-072, KB-079, KB-091
- **Potential Visual:** رسالة واتساب مبهمة («لازم نتكلم») تتحول إلى رسالة واضحة («ممكن نتكلم 10 دقايق بكرة الساعة 11 عن تسليم المشروع؟»).
- **Potential Exercise:** أعد كتابة 3 رسائل مبهمة كطلبات محددة.
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 56

### KB-076 · النقد مقابل الشكوى — وصيغة XYZ | Criticism vs. Complaint; the XYZ Formula
- **Definition:** جوتمان: النقد القاسي علامة الإنذار المبكرة — «اغتيال للشخصية، انتقاد للشخص نفسه، وليس لفعل ما» («أناني لا تفكر إلا في نفسك»). الشكوى: «أنا شعرت عندما نسيت… بأنك لا تهتم بي» — «تعبير جازم وليس رغبة في الهجوم». حاييم جينوت — **XYZ**: «عندما تفعل X، أشعر بـY، وكنت أفضل أن تفعل Z» — بدل «أنت مهمل، كاذب وأناني».
- **Book:** Goleman (عن جوتمان وجينوت)
- **Chapter:** ف9
- **Page:** ص193–196، ص210–211
- **Example:** «عندما لم تتصل بي… شعرت بالغضب… كنت أتمنى أن تتصل» (ص210–211).
- **Application:** النسخة «السريعة» في CASE 2. **[BOOK DIFFERENCE]**: عبارة «شعرت… بأنك لا تهتم بي» في مثال جوتمان تُعد في NVC «شعورًا زائفًا/تقييمًا» (L997–1017)، وXYZ لا يفصل الاحتياج ولا يصوغ الطلب بصيغة فعل حالي محدد كما في NVC ⇒ نقدم XYZ كخطوة أولى وNVC كنسخة أدق.
- **Related Concepts:** KB-072, KB-036, KB-093
- **Potential Visual:** سهم يضرب «الشخص» (نقد) مقابل سهم يشير إلى «الفعل» (شكوى).
- **Potential Exercise:** حوّل 3 انتقادات إلى شكاوى XYZ ثم إلى NVC — ولاحظ الفرق.
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE] + [BOOK DIFFERENCE]
- **CT#:** 170, 173

### KB-077 · النقد البارع — للمُرسل والمتلقي | Artful Critique
- **Definition:** «النقد هو المهمة الأولى» للمدير؛ أسوأ طريقة: «أنت أحمق ولا فائدة ترجى منك»؛ وتأجيل الملاحظات يراكم الإحباط حتى «انفجار… بنبرة تهكمية، مع استرجاع قائمة طويلة من شكواهم المختزنة». **هاري ليفنسون**: (1) كن محددًا (2) قدّم حلًا (3) كن حاضرًا — وجهًا لوجه على انفراد (4) كن حساسًا. للمتلقي: النقد معلومة، راقب اندفاعك الدفاعي، اطلب لقاءً لاحقًا بعد الهدوء.
- **Book:** Goleman
- **Chapter:** ف10 «التحكم بالعاطفة»
- **Page:** ص215–221
- **Example:** المهندس ونائب الرئيس المتهكم «متى تخرجت في الجامعة؟! هذه المواصفات مضحكة» ← أسبوع من الاجترار ← سؤال محسوب ← اتضح أن الرأي الحقيقي إيجابي، فاعتذر (ص215–217).
- **Application:** **CASE 1** بالكامل (الطرفان): ماذا كان على المدير أن يفعل (ليفنسون)، وماذا يفعل الموظف (KB-067 + سؤال المهندس).
- **Related Concepts:** KB-067, KB-064, KB-089
- **Potential Visual:** بطاقة من 4 خانات «النقد البارع» تُملأ أثناء إعادة تمثيل المشهد.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]
- **CT#:** 176

### KB-078 · التوكيد: الطريق الأوسط | Assertion
- **Definition:** «the middle road between being aggressive and passively allowing someone to take advantage of us… stand up for ourselves without attacking the other person». الرد على «يا غبي»: عدواني «If you think I'm stupid, you are an idiot!» / **توكيدي** «(calm and firm) You might think I'm stupid, but let's get back to the real issue, which is XYZ» / سلبي (رأس منكس، صمت). أربع استراتيجيات: (1) عبارات «أنا» بدل «أنت» اللوامة (2) **اعترف بأي حقيقة في الشكوى وفي نفس الوقت دافع عن حقك** (3) عبّر بوضوح عن احتياجك بدل انتظار قراءة الأفكار (4) ركّز على عملية التوكيد لا النتيجة — «The goal of assertion is clear communication». التوكيد «can reduce the frequency of being treated unfairly or being taken advantage of».
- **Book:** MoM
- **Chapter:** Ch.15
- **Page:** p.261–262
- **Example:** «I'm really tired and need a few minutes to myself…» عند العودة من العمل للأطفال (p.262).
- **Application:** أداة مركزية للمرحلتين 5 و7. تمثل صيغة الـBrief **«NOT ATTACK / NOT SUBMIT»** من مصدر مزود (MoM) — وتلتقي مع CC «Sucker's Choice» (KB-086).
- **Related Concepts:** KB-086, KB-103, KB-095, KB-079
- **Potential Visual:** ثلاثة أوضاع جسد (هجوم مائل للأمام — واقف مستقيم هادئ — منكمش) — تتكرر في Dark EQ.
- **Potential Exercise:** «رد بالطريقة التوكيدية» على 3 جمل مستفزة.
- **Tag:** [DIRECT SOURCE]؛ ربطه بالـBrief = [INTEGRATED SYNTHESIS]
- **CT#:** 139

### KB-079 · «لو بتحبني هتعرف لوحدك» | "If You Care, You'll Know What I Want"
- **Definition:** افتراض علاقاتي: «If you care, then you will know what I want without me asking» مقابل «If you want something, then you will let me know». ضمن افتراضات تعيق التوكيد: «If you really like/love me, then you will know what I need»، «People won't like me if I say no»، «It's not worth the argument»، «I can live with this».
- **Book:** MoM
- **Chapter:** Ch.11، Ch.15
- **Page:** p.134، p.263
- **Example:** —
- **Application:** CASE 2 (خلاف زوج وزوجة) — جملة شديدة القرب من الثقافة المصرية («المفروض تحس بيا من غير ما أقول»). ويلتقي مع NVC «الطلبات الواضحة».
- **Related Concepts:** KB-051, KB-075, KB-078
- **Potential Visual:** شخصان كل منهما يحمل لافتة مقلوبة لا يراها الآخر.
- **Potential Exercise:** «اكتب حاجة كنت مستني حد يعرفها لوحده… وحوّلها لطلب».
- **Tag:** [DIRECT SOURCE]؛ الالتقاء مع NVC = [INTEGRATED SYNTHESIS]
- **CT#:** 124

### KB-080 · التقدير والامتنان — للاحتفاء لا للتلاعب | Appreciation & Gratitude
- **Definition:** NVC: المديح «positive judgment»؛ مديرون استخدموا المديح لأنه «يرفع الإنتاجية» فانخفضت حين «sense the manipulation behind the appreciation» ⇒ **«Express appreciation to celebrate, not to manipulate»**. التقدير الصادق = الفعل + الاحتياج الذي لُبي + الشعور. MoM: «Gratitude does not have to mean ignoring negative things»؛ يوميات امتنان (5 دقائق أسبوعيًا)؛ التعبير عن الامتنان للآخرين «may deepen our gratitude experience and improve our relationships»؛ «gratitude plays a role in every major religion».
- **Book:** NVC · MoM
- **Chapter:** NVC Ch.14؛ MoM Ch.12
- **Page:** NVC L3670–3694، L3753–3767؛ MoM p.175–185
- **Example:** NVC: «98% perfect… 2% I'll remember» — «We tend to notice what's wrong rather than what's right». MoM: لويزا تطلب إعادة تسخين الطعام وتظل ممتنة (p.176).
- **Application:** يوم 7 في خطة الأيام السبعة (رسالة شكر). وفي Dark EQ: الفرق بين التقدير الصادق والمديح المتلاعب (KB-105).
- **Related Concepts:** KB-105, KB-069, KB-133
- **Potential Visual:** ورقة شكر مكتوبة بخط اليد تتحول إلى موجة ضوء.
- **Potential Exercise:** «ابعت رسالة شكر محددة لحد: عملت إيه… لبّى إيه عندي… حسيت بإيه».
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]
- **CT#:** 71, 130

### KB-081 · الاعتذار والإصلاح | Apology & Repair
- **Definition:** MoM: قالب الاعتذار: «I realize when I ___, this hurt you. This was wrong because ___. I'm sorry I did this. I want to do ___ to let you know how truly sorry I am, and I hope that you can forgive me in time» — مع «no guarantee that the person will do so». CC: الاعتذار الصادق «requires change of heart» والتخلي عن حفظ ماء الوجه؛ «You can't unring the bell». Goleman: «آليات الإصلاح» في الزيجات الطويلة = «ترموستات عاطفي»؛ تحمل المسؤولية «أو حتى تعتذر» (ص205–210).
- **Book:** MoM · CC · Goleman
- **Chapter:** MoM Ch.15؛ CC Ch.5، Ch.11؛ Goleman ف9
- **Page:** MoM p.275–276؛ CC p.76، p.209–210؛ Goleman ص205–210
- **Example:** فيك: «10/9 – Lost my temper and shouted at Judy. At least I apologized later» (MoM p.124).
- **Application:** خطوة REPAIR داخل NAVIGATE؛ وفي نهاية CASE 2. الاعتذار لا يُلزم الآخر بالمسامحة — نقطة أخلاقية.
- **Related Concepts:** KB-088, KB-119, KB-135
- **Potential Visual:** كوب مكسور يُرمم بخيوط ذهبية.
- **Potential Exercise:** املأ قالب الاعتذار لموقف حقيقي (لا يُرسل إلا إذا أردت).
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 143, 18

---

# المرحلة 6 — HANDLE CONFLICT | أدِر الخلاف تحت الضغط
*العمود الفقري: Goleman ف9–10 (تطبيق الذكاء العاطفي في الزواج والعمل). الأداة الرئيسية: Crucial Conversations. داعم: NVC ف11 + MoM ف10، 15.*

### KB-082 · المحادثة الحاسمة | Crucial Conversation
- **Definition:** «A discussion between two or more people where (1) stakes are high, (2) opinions vary, and (3) emotions run strong». ثلاث طرق للتعامل: نتجنبها، نواجهها بشكل سيئ، نواجهها بشكل جيد. «When conversations matter the most… we're generally on our worst behavior». CC يشرح ذلك بيولوجيًا بتبسيط: «We're designed wrong» (الأدرينالين والدم للعضلات).
- **Book:** CC
- **Chapter:** Ch.1
- **Page:** p.3–5
- **Example:** أمثلة الكتاب: مناقشة ترقية، استراتيجية تسويق، شك الزوج في مغازلة، سور الجار (p.1–3).
- **Application:** افتتاح المرحلة 6 وتعريف CASE 3 (مقاول ومدير مشروع). الربط بـGoleman (النوبة الانفعالية) = [INTEGRATED SYNTHESIS].
- **Related Concepts:** KB-007, KB-083, KB-084
- **Potential Visual:** ثلاثة مؤشرات ترتفع معًا: «الرهان» — «الاختلاف» — «المشاعر».
- **Potential Exercise:** **Exercise 7 (أ)**: «اكتب محادثة حاسمة مأجلها».
- **Tag:** [DIRECT SOURCE]
- **CT#:** 3, 4, 5

### KB-083 · الحوار وحوض المعنى المشترك | Dialogue & the Pool of Shared Meaning
- **Definition:** الحوار = «The free flow of meaning between two or more people»؛ كل طرف يضيف معناه إلى **حوض المعنى المشترك** — «measure of a group's IQ». «individually smart people can do collectively stupid things». Samuel Butler (يقتبسه CC): «He that complies against his will is of his own opinion still».
- **Book:** CC
- **Chapter:** Ch.2
- **Page:** p.20–23
- **Example:** مريض دخل لاستئصال اللوزتين فأُجريت له عملية في القدم؛ 7 أشخاص لاحظوا ولم يتكلموا (p.22) — «people hold back rather than anger someone in power».
- **Application:** الاستعارة البصرية الرئيسية لـAnimation 7. وقصة المستشفى + جملة Butler تتكرران في Dark EQ: الصمت أمام السلطة، والامتثال ≠ الموافقة.
- **Related Concepts:** KB-084, KB-107, KB-124
- **Potential Visual:** حوض ماء في المنتصف؛ أكواب ملونة من كل طرف تصب فيه؛ طرف يمسك كوبه ولا يصب (صمت).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]
- **CT#:** 7

### KB-084 · الصمت والعنف | Silence vs. Violence
- **Definition:** عند غياب الأمان نميل للصمت أو العنف. **الصمت**: التقنيع (سخرية، تجميل، تلطيف)، التجنب، الانسحاب. **العنف**: «any verbal strategy that attempts to convince, control, or compel others to your point of view» — السيطرة (المقاطعة، المبالغة، المطلقات، تغيير الموضوع، الأسئلة الموجِّهة)، الوصم، الهجوم (التحقير، التهديد). وفي Ch.2: العنف يشمل «anything from subtle manipulation to verbal attacks… We borrow power from the boss».
- **Book:** CC
- **Chapter:** Ch.2، Ch.4
- **Page:** p.24، p.51–54
- **Example:** «Salute and Stay Mute»، «Freeze Your Lover» (p.24).
- **Application:** Animation 7 وCASE 3. **CC يعدّ التلاعب صراحة شكلًا من «العنف»** ⇒ جسر مصدري مباشر لـDark EQ. وعبارة «We borrow power from the boss» تُستخدم في تحليل «استعارة السلطة» في حالة عتمان.
- **Related Concepts:** KB-083, KB-087, KB-093, KB-097
- **Potential Visual:** مسطرة أفقية: طرف أزرق (صمت) وطرف أحمر (عنف) والمنتصف أخضر (حوار).
- **Potential Exercise:** «أنا بروح لأنهي ناحية تحت الضغط؟» (نسخة مختصرة من Style Under Stress، p.56–62 — لا يُنسخ الاختبار كاملًا).
- **Tag:** [DIRECT SOURCE]
- **CT#:** 8, 15

### KB-085 · ابدأ بالقلب — الأسئلة الأربعة | Start with Heart
- **Definition:** «Work on me first»: «the only person we can continually inspire, prod, and shape… is the person in the mirror». تحت الأدرينالين تتحول الدوافع إلى: حفظ ماء الوجه، الفوز، إثبات الصواب، العقاب — «When adrenaline does our thinking for us, our motives flow with the chemical tide». **الأسئلة الأربعة**: ماذا أريد حقًا لنفسي؟ للآخر؟ للعلاقة؟ كيف كنت سأتصرف لو كنت أريد هذا فعلًا؟ «when you name the game, you can stop playing it».
- **Book:** CC
- **Chapter:** Ch.3
- **Page:** p.29–37
- **Example:** ★ Greta المديرة التنفيذية: سؤال علني عن أثاث بـ150 ألف دولار ← تحمر وتتجمد ← نفس عميق ← «What do I really want here?» ← تشكر السائل (p.30–33).
- **Application:** **Exercise 7** (المحادثة الصعبة) و**CASE 1** (من جهة المدير). الأسئلة الأربعة = «NAVIGATE» في الإطار النهائي.
- **Related Concepts:** KB-024, KB-086, KB-089
- **Potential Visual:** بوصلة بأربعة اتجاهات: أنا — هو — العلاقة — السلوك.
- **Potential Exercise:** **Exercise 7 (ب)**: أجب عن الأسئلة الأربعة لمحادثتك المؤجلة.
- **Tag:** [DIRECT SOURCE]
- **CT#:** 9, 10, 11

### KB-086 · اختيار المغفل والبحث عن «و» | The Sucker's Choice & the "And"
- **Definition:** «اختيار المغفل» ثنائية زائفة: «إما أن أكون صريحًا وأهاجم، أو أكون لطيفًا وأصمت». الحل — ابحث عن «و»: وضّح ما تريد، ووضّح ما لا تريد، ثم اجمعهما في سؤال واحد: «كيف أقول … **و** أتجنب …؟». «you don't have to choose between being honest and being effective». «Is this really possible?» — هل تعرف أحدًا يستطيع؟
- **Book:** CC
- **Chapter:** Ch.1، Ch.3
- **Page:** p.9، p.37–41
- **Example:** برنت ورويس «fossil» — «I'm the only one around who has the guts to speak the truth» (p.37–39).
- **Application:** الأساس المصدري من CC لشعار الـBrief **«NOT ATTACK · NOT SUBMIT»** في Dark EQ؛ يلتقي مع التوكيد في MoM (KB-078).
- **Related Concepts:** KB-078, KB-085, KB-095
- **Potential Visual:** مفترق طرق بلافتتين «هجوم» و«خضوع» — ثم يظهر طريق ثالث في المنتصف مكتوب عليه «و».
- **Potential Exercise:** «اكتب جملة "و"»: «إزاي أقول لمديري إن التاسك ده مش هيخلص **و** أحافظ على ثقته فيّ؟».
- **Tag:** [DIRECT SOURCE]؛ ربطه بالـBrief = [INTEGRATED SYNTHESIS]
- **CT#:** 12

### KB-087 · الأمان: الهدف المشترك والاحترام المتبادل | Safety: Mutual Purpose & Mutual Respect
- **Definition:** «nothing kills the flow of meaning like fear»؛ «if you make it safe enough, you can talk about almost anything». الأمان يقوم على **الهدف المشترك** (شرط الدخول) و**الاحترام المتبادل** (شرط الاستمرار): «respect is like air. If you take it away, it's all people can think about». و**«Mutual Purpose is not a technique… If our goal is to get our way or manipulate others, it will quickly become apparent, safety will be destroyed»**.
- **Book:** CC
- **Chapter:** Ch.4، Ch.5
- **Page:** p.49–51، p.69–74
- **Example:** إضراب نقابة/إدارة: قائمتا أهداف متطابقتان تقريبًا (p.73–74).
- **Application:** CASE 3 (المقاول ومدير المشروع: الهدف المشترك = تسليم المشروع بأمان وفي الموعد). وجملة «Mutual Purpose is not a technique» = الحد الأخلاقي في Dark EQ.
- **Related Concepts:** KB-083, KB-084, KB-088, KB-097
- **Potential Visual:** حلقة أمان حول الحوض؛ تنكسر عند «تدوير العين» وتلتئم عند «هدف مشترك».
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]
- **CT#:** 14, 16, 17

### KB-088 · المقابلة (Contrasting) وCRIB — والاعتذار | Contrasting, CRIB, Apologize
- **Definition:** **الاعتذار** عند انتهاك الاحترام. **المقابلة**: «لا أقصد… / أقصد…» — توضح السياق والتناسب، و«Contrasting is not apologizing». **CRIB** عند تعارض الأهداف: Commit (التزم بالبحث عن هدف مشترك) — Recognize (اعرف الغرض وراء الاستراتيجية: «Why do you want that?») — Invent (ابتكر هدفًا أعلى) — Brainstorm (استراتيجيات جديدة). الأسوأ: المنافسة أو الخضوع؛ الجيد: التسوية؛ الأفضل: CRIB. تحذير من «false dialogue… calmly arguing our side until the other person gives in».
- **Book:** CC
- **Chapter:** Ch.5
- **Page:** p.76–88
- **Example:** يوتام وإيفون (العلاقة الحميمة والتبويز) — يوتام يعترف: «I pout because I'm hurting. And I also do it hoping it'll make you feel bad» (p.88–90).
- **Application:** CASE 3 وCASE 2. **[BOOK DIFFERENCE D2]**: CC يقبل التسوية كحل «جيد»، وNVC يستهدف «satisfaction instead of compromise» (L3060)، وMoM في المنتصف (يرفض التنازل «just to avoid conflict» ويقبل ما يلبي احتياجات الطرفين، p.172–173). ومثال يوتام يُستخدم في Dark EQ (الانسحاب كضغط — KB-104).
- **Related Concepts:** KB-087, KB-096, KB-104
- **Potential Visual:** قالب «لا أقصد ❌ / أقصد ✅» على الشاشة.
- **Potential Exercise:** اكتب جملة Contrasting لموقف فهمك فيه حد غلط.
- **Tag:** [DIRECT SOURCE] + [BOOK DIFFERENCE D2]
- **CT#:** 18

### KB-089 · STATE — كيف أقول رأيي الصعب | STATE My Path
- **Definition:** **S**hare your facts — **T**ell your story — **A**sk for others' paths — **T**alk tentatively — **E**ncourage testing. ابدأ بالحقائق (أقل إثارة للخلاف وأكثر إقناعًا)؛ «Gathering the facts is the homework required for crucial conversations». تحدث بتردد مقصود («I'm beginning to wonder if…») — «the more forceful we are, the less persuasive we are» — دون أن تعتذر عن رأيك. اختبار **Goldilocks**: شديد النعومة / شديد القسوة / مضبوط.
- **Book:** CC
- **Chapter:** Ch.7
- **Page:** p.124–135
- **Example:** ★ بوب وكارول وفاتورة «Good Night Motel»: «I can't believe you're doing this to me!» — ثم تبيّن أن صاحب المطعم الصيني يملك الموتيل وآلة الطبع واحدة (p.122–123، p.135–136).
- **Application:** **Exercise 7** والنسخة العملية من COMMUNICATE تحت الضغط؛ وفي Dark EQ: «STATE FACTS» في سلسلة CC المطلوبة في الـBrief.
- **Related Concepts:** KB-043, KB-085, KB-090, KB-095
- **Potential Visual:** 5 درجات سلم (S-T-A-T-E) + ثلاث أوعية Goldilocks.
- **Potential Exercise:** **Exercise 7 (ج)**: اكتب أول جملتين من محادثتك بصيغة Facts + Tentative story.
- **Tag:** [DIRECT SOURCE]
- **CT#:** 27, 28

### KB-090 · استكشف مسار الآخر: AMPP وABC | Explore Others' Paths
- **Definition:** **AMPP**: **A**sk («What's going on?»)، **M**irror (عكس المشاعر حين لا تتسق النبرة مع الكلام)، **P**araphrase (قصته بكلماتك)، **P**rime (تخمين جريء حين يصمت). عند الاختلاف **ABC**: **A**gree (فيما تتفقان)، **B**uild (أضف ما ينقص)، **C**ompare (قارن حين تختلفان) — أغلب الخلافات على 5–10% («violent agreement»).
- **Book:** CC
- **Chapter:** Ch.8
- **Page:** p.148–158
- **Example:** ويندي (الابنة) وصديقها المقلق: Apologize، Ask، Mirror، Paraphrase، Prime ← «Why am I so ugly?» (p.154–156).
- **Application:** CASE 2 وCASE 3 — وتلتقي مع NVC (إعادة الصياغة) وGoleman (الانعكاس) (KB-062).
- **Related Concepts:** KB-062, KB-064, KB-065
- **Potential Visual:** أربع أيقونات AMPP (علامة استفهام، مرآة، فقاعة كلام، مضخة).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 30

### KB-091 · من يقرر؟ ومن يفعل ماذا ومتى؟ — ووثّق | Decide How to Decide; WWWF; Document
- **Definition:** الحوار ≠ اتخاذ القرار. أربع طرق: أمر، استشارة، تصويت، إجماع. **«Don't pretend to consult»** (استشارة شكلية). ثم **Who does What by When + Follow-up** — «there is no 'we'». **«Document your work… One dull pencil is worth six sharp minds»**: اكتب الاستنتاجات والقرارات والمهام.
- **Book:** CC
- **Chapter:** Ch.9
- **Page:** p.161–177
- **Example:** قضية الإخوة وتقسيم تركة الأم: «I've kept a record of all the expenses» (p.188–192).
- **Application:** خاتمة CASE 3 (محضر اجتماع بسيط). و**أساس بند الدرع «وثّق الأمور المهمة»** — التطبيق على مواقف التلاعب = [INTEGRATED SYNTHESIS] لأن سياق CC هو المحاسبة والقرارات.
- **Related Concepts:** KB-089, KB-125, KB-107
- **Potential Visual:** دفتر صغير وقلم رصاص — جدول 4 أعمدة: مين / إيه / إمتى / متابعة.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ تطبيقه في Dark EQ = [INTEGRATED SYNTHESIS]
- **CT#:** 32, 33, 34

### KB-092 · الطوفان والوقت المستقطع | Flooding & Timeouts
- **Definition:** Goleman (جوتمان): «طفح الكيل/الطوفان» — سلبية الطرف الآخر «تسحقنا» فلا نستمع «بعقل صافٍ»؛ يبدأ مع زيادة ~10 نبضات فوق معدل الهدوء؛ الغارق يصبح «شديد الحذر لأي علامة… هجوم». الأداة: قياس النبض، وعند +10 **استراحة 20 دقيقة** («5 دقائق لا تكفي»)، واتفاق مسبق على الوقت المستقطع. MoM: الوقت المستقطع «as athletes do: to regroup, strategize, relax» — من **5 دقائق إلى 24 ساعة**؛ «The timeout is not used to avoid a situation, but rather to enable you to approach the situation from a new angle». **ترمومتر فيك 0–10**: عند 3 ← «أحتاج استراحة دقائق»؛ عند 5 ← استراحة + سجل أفكار + «Write out what I hear Judy saying… Show Judy this summary»؛ فوق 5 ← استراحة أطول والعودة تحت 3. CC: «Coming to mutual agreement to take a time-out is not the same thing as going to silence»؛ ولا تقل لغيرك «اهدأ». NVC: الانسحاب الجسدي المؤقت لتعاطف الذات.
- **Book:** Goleman · MoM · CC · NVC
- **Chapter:** Goleman ف9؛ MoM Ch.10، Ch.15؛ CC Ch.11؛ NVC Ch.7
- **Page:** Goleman ص200–208؛ MoM p.121–124، p.261؛ CC p.206–207؛ NVC L2177–2199
- **Example:** «حبيبي لازم نتكلم» تُسمع عند الغارق كـ«تريد أن نتعارك مرة ثانية» (Goleman ص201).
- **Application:** أداة REGULATE/NAVIGATE الرئيسية في CASE 2. **[BOOK DIFFERENCE D7]**: مدة التهدئة — Goleman: 20 دقيقة على الأقل؛ MoM: 5 دقائق–24 ساعة. **[BOOK DIFFERENCE D5]**: ثلاثة أنواع «خروج» — استراحة للعودة (أداة)، تجنب (يزيد القلق — KB-014)، ابتعاد عن مسيء (حماية — KB-117).
- **Related Concepts:** KB-010, KB-037, KB-060, KB-117
- **Potential Visual:** ترمومتر 0–10 بعلامات 3 و5 + ساعة رملية 20 دقيقة + لافتة «هرجع».
- **Potential Exercise:** «اتفاق الاستراحة»: جملة جاهزة يتفق عليها الطرفان مسبقًا — «أنا محتاج 20 دقيقة وهرجع نكمل».
- **Tag:** [DIRECT SOURCE] (4 كتب) + [REPORTED IN SOURCE] + [BOOK DIFFERENCE D5, D7]
- **CT#:** 172, 121, 138, 40

### KB-093 · أسلحة جوتمان الأربعة | Criticism, Contempt, Defensiveness, Stonewalling
- **Definition:** النقد القاسي (اغتيال الشخصية)، **الاحتقار** (السخرية، لي الشفتين، تدوير العينين — «حكم صامت على أسوأ ما يراه في الطرف الآخر»)، الدفاعية، ثم **تجميد المناقشة** (Stonewalling): انسحاب بلا تعبير = «التباعد والتعالي والنفور».
- **Book:** Goleman (عن جوتمان)
- **Chapter:** ف9
- **Page:** ص193–197
- **Example:** باميلا وتوم: «أناني لا تفكر إلا في نفسك» (ص194).
- **Application:** CASE 2. تسمية «الفرسان الأربعة» = [EXTERNAL KNOWLEDGE] (Goleman لا يستخدمها). و«التجميد» يُعاد في Dark EQ كـ«الصمت العقابي» (KB-104) مع التمييز بين انسحاب الغارق (حماية ذاتية) والانسحاب المقصود للضغط.
- **Related Concepts:** KB-076, KB-084, KB-104
- **Potential Visual:** 4 أيقونات تظهر بالتتابع فوق حوار زوجين؛ مؤشر «بعد المسافة» يكبر.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]؛ التسمية = [EXTERNAL KNOWLEDGE]
- **CT#:** 170

### KB-094 · النمط مقابل الواقعة | Pattern vs. Instance
- **Definition:** CC: في المرة الأولى تكلم عن **المحتوى**؛ عند التكرار تكلم عن **النمط** (الالتزام)؛ ثم عن **العلاقة** (الثقة/الاحترام) — «Groundhog Day»: تحدث عن النمط لا عن آخر حادثة. ومع «word games» ومن لديه أعذار لا تنتهي: تحدث عن النمط والسلوكيات والنتائج. MoM يحذر من «وضع الناس في صناديق» بعد موقف واحد (p.259).
- **Book:** CC · MoM
- **Chapter:** CC Ch.11؛ MoM Ch.15
- **Page:** CC p.205–208، p.211–212؛ MoM p.259
- **Example:** زميل يتأخر في التسليم للمرة الرابعة: الحديث عن «الالتزام» لا عن «تقرير الخميس».
- **Application:** **الأساس المصدري لقاعدة الـBrief «ONE INCIDENT vs REPEATED PATTERN»** في Dark EQ (CC يستخدمها للمحاسبة؛ تطبيقها على كشف التلاعب = [INTEGRATED SYNTHESIS]).
- **Related Concepts:** KB-057, KB-114, KB-127
- **Potential Visual:** نقطة واحدة على خط زمني (واقعة) ← نقاط متكررة بنفس الشكل (نمط) ← خط يربطها.
- **Potential Exercise:** جزء من **Exercise 8**: «واقعة ولا نمط؟» — 4 سيناريوهات.
- **Tag:** [DIRECT SOURCE]؛ التطبيق على Dark EQ = [INTEGRATED SYNTHESIS]
- **CT#:** 39, 42

### KB-095 · عبارة الحد الهادئة | Calm Statement of a Line
- **Definition:** CC (تجاوز الاحترام): «Show zero tolerance… Speak up immediately, but respectfully… 'The way you're leaning in toward me and raising your voice seems disrespectful.'» — وصف سلوكي + أثر، بلا إهانة. Goleman (برنامج لوكمان): الطفل الذي «حملق… وقال له: لا تفعل هذا مرة ثانية، ثم واصل السير» = سيطرة + احتفاظ بتقدير الذات دون عراك (ص327–328).
- **Book:** CC · Goleman
- **Chapter:** CC Ch.11؛ Goleman ف15
- **Page:** CC p.208–209؛ Goleman ص327–328
- **Example:** CC (التحرش): الحقائق أقوى من الاتهام العام: «I want you to stop sexually harassing me!» مقابل وصف محدد للسلوك (p.126).
- **Application:** **قالب الحدود** في المرحلة 7: «لما [سلوك محدد]، ده بالنسبة لي [أثر]. أنا مستعد نكمل الكلام لما…». يلتقي مع صيغة الـBrief (NVC في موقف حدود).
- **Related Concepts:** KB-078, KB-086, KB-122, KB-125
- **Potential Visual:** وضعية «الجبل» (KZ) مع فقاعة الجملة الهادئة.
- **Potential Exercise:** اكتب جملة حد هادئة لموقف تكرر معك.
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 41

### KB-096 · حل النزاع بالاحتياجات — خمس خطوات | NVC Conflict Resolution
- **Definition:** (1) عبّر عن احتياجاتك (2) ابحث عن احتياجات الآخر الحقيقية أيًا كانت صياغته (3) تحقق أنك سمعتها بدقة (4) قدّم التعاطف اللازم (5) اقترح استراتيجيات بلغة فعل إيجابية («Would you be willing to…»). **الاحتياجات ≠ الاستراتيجيات**: «I need to get out of this marriage» = استراتيجية. «People often need empathy before they are able to hear what is being said». الهدف «satisfaction instead of compromise» — ادعاء المؤلف أنه ممكن «to resolve just about any conflict».
- **Book:** NVC
- **Chapter:** Ch.11
- **Page:** L3044–3192
- **Example:** ★ خلاف 39 سنة حول دفتر الشيكات حُل في أقل من 20 دقيقة حين سُمعت الاحتياجات: هو «حماية الأسرة»، هي «أن تُمنح الثقة» (L3150–3192).
- **Application:** CASE 2 (الزوجين) — القصة قابلة للتمصير مباشرة («مين يمسك الفلوس»). **[BOOK DIFFERENCE D2]** مع CC حول التسوية (KB-088).
- **Related Concepts:** KB-063, KB-088, KB-072
- **Potential Visual:** طرفان يشد كل منهما حبلًا (استراتيجيات) ← تحت الأرض جذران يلتقيان (احتياجات).
- **Potential Exercise:** «الاحتياج ورا الطلب»: لكل طرف في CASE 2 — طلبه ← احتياجه.
- **Tag:** [DIRECT SOURCE] + [BOOK DIFFERENCE D2]
- **CT#:** 67

---

# المرحلة 7 — PROTECT YOURSELF | احمِ نفسك (Dark EQ Shield)
*العمود الفقري: Goleman — الجانب المظلم لنفس المهارات (ف3، ف5، ف7، ف8، ف10، ف12، ف13، ف15). داعم: MoM ف3، 9، 12، 14، 15 · NVC ف2، 5، 6، 10، 12، 14 · KZ · CC ف2، 5، 11 · FILM.*

> **قواعد إلزامية لكل مداخل هذه المرحلة** (من الـBrief):
> 1. الغرض **الكشف + الحماية + الحدود + الاستخدام الأخلاقي** — لا توجد هنا أي «خطوات تنفيذ» للتلاعب؛ كل تكتيك يُوصف بـ«كيف يظهر / كيف تتعرف عليه / كيف تحمي نفسك» فقط.
> 2. **لا تشخيص**: نقول «هذا سلوك تلاعبي» لا «هو نرجسي/سايكوباتي».
> 3. **ONE INCIDENT ≠ REPEATED PATTERN** (KB-094).
> 4. عتمان **FICTIONAL / DRAMATIC CASE STUDY** — لا دوافع ولا مشاهد غير مدعومة (FILM §6).
> 5. [SAFETY]: الإساءة الجسدية/الجنسية ⇒ إحالة لجهة مساعدة، لا «تقنيات تواصل».

### KB-097 · «الذكاء العاطفي المظلم» كمصطلح | "Dark EQ" as a Teaching Frame
- **Definition:** إطار تعليمي لوصف **الاستخدام الاستغلالي لفهم المشاعر والدوافع**: أفهمك ← أتعرف على مخاوفك واحتياجاتك ← أستخدمها للضغط والسيطرة (مقابل: أفهمك ← أتعاطف ← أحترم حدودك ← أتواصل). **المصطلح نفسه غير موجود في الكتب الخمسة**، ولا يُقدَّم كتشخيص نفسي رسمي. لكن الفكرة لها جذور مباشرة في Goleman: وجهة نظر «أكثر تشاؤمًا» في عهد ثورندايك رأت الذكاء الاجتماعي «قدرة على خداع الآخرين وجعلهم يفعلون ما تريد سواء بإرادتهم أو رغمًا عنهم» (ص65–66)؛ وتعريف المجال الخامس «فن العلاقات… هو في معظمه مهارة في تطويع عواطف الآخرين» (ص68) مهارة مزدوجة الاستخدام؛ و«هذه المهارات يمكن أيضًا استخدامها لإغاظة أخ أو الإضرار به» (ص167).
- **Book:** Goleman (الجذور) + إطار الـBrief
- **Chapter:** ف3، ف8
- **Page:** ص65–68، ص167
- **Example:** الطفل «جاي» (سنتان ونصف) يجرب مخزون تكتيكات لتهدئة أخيه — طلب، حليف، ربت، إلهاء، تهديد، أمر — تقليدًا لما عومل به (ص165–166): نفس الأدوات يمكن أن تهدّئ أو تضغط.
- **Application:** تعريف افتتاحي لموديول Dark EQ (12–18 دقيقة). جملة المفتاح: «المشكلة مش إنك تعرف تقرا الناس… المشكلة في اللي هتعمله باللي قريته» [USER-PROVIDED FRAMEWORK].
- **Related Concepts:** KB-098 → KB-132, KB-001, KB-084
- **Potential Visual:** Animation 8 «Dark EQ»: سهم واحد «أفهمك» ينقسم إلى مسارين — أخضر (تعاطف ← حدود ← تواصل) وأحمر (مخاوف ← ضغط ← سيطرة)؛ المسار الأحمر يُعرض **مشطوبًا/كتحذير** لا كطريقة.
- **Potential Exercise:** —
- **Tag:** [USER-PROVIDED FRAMEWORK] (المصطلح) + [DIRECT SOURCE] (جذور Goleman) + [NOT SUPPORTED BY PROVIDED SOURCE] (المصطلح «Dark EQ» كلفظ)
- **CT#:** — (جديد)؛ مرتبط 150، 166

### KB-098 · الانفعال المصطنع كأداة ضغط | Performed Emotion as Leverage
- **Definition:** Goleman ينقل عن ديان تايس: «بعض الناس الميكيافيليين تمامًا فيما يتعلق بالأمزجة المخادعة… المحصلين الذين يتعمدون إظهار الغضب ليضفوا على أنفسهم مظهر الحازم» (ص89). وإيكمان: «التعبير المبالغ فيه» كخدعة — الطفلة التي تغيّر وجهها تمثيليًا وهي تجري لتشكو لأمها (ص168)؛ و«الانفعالات تكون وسيلة ورسالة في الوقت نفسه». وفي ص46 ذكر عابر لـ«مخزون… من الحيل الانفعالية: … استدرار العطف… التحريض… التظاهر كذبًا بالشجاعة».
- **Book:** Goleman
- **Chapter:** ف2، ف5، ف8
- **Page:** ص46، ص89، ص167–168
- **Example:** (كيف يظهر) غضب يرتفع فجأة عند طلب حقك ويختفي فور تنازلك؛ دموع/شكوى تظهر كلما اقتربت من «لا».
- **Application:** **كيف تتعرف**: الانفعال «يشتغل» بنتيجة ثابتة (تنازلك) ويتكرر بنفس التوقيت — نمط لا واقعة (KB-094). **كيف تحمي نفسك**: الدرع بند 2 «لا تقرر تحت الخوف أو الذنب» + بند 7 «لا تدخل لعبة الانفعال» + قاعدة CC: التعاطف مع الانفعال ≠ الامتثال (KB-065).
- **Related Concepts:** KB-065, KB-094, KB-103, KB-129
- **Potential Visual:** قناع مسرحي غاضب يُرفع ليكشف وجهًا هادئًا ينظر إلى «النتيجة».
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]؛ صياغة «كيف تتعرف/تحمي» = [INTEGRATED SYNTHESIS]
- **CT#:** 166

### KB-099 · التخويف المحسوب للسيطرة | Calculated Intimidation for Control
- **Definition:** Goleman: فئة من المعتدين على زوجاتهم «يزدادون هدوءًا كلما زادت عدوانيتهم» (ينخفض النبض)؛ و«هذا الفعل الإرهابي المحسوب من العنف هو وسيلة للسيطرة… بغرس الخوف» (ص160–161) — تخويف محسوب ≠ نوبة غضب. و«نظرة التخويف» في بيئات العصابات (ص159–160)، و«المهارة الانفعالية المنحرفة، مثل تخويف الناس» (ص160). **تحذير Goleman نفسه**: لا توجد «علامة بيولوجية» للجريمة ولا عامل وراثي، ومعظم من لديهم نقص تعاطف لا ينحرفون (ص161 حاشية).
- **Book:** Goleman
- **Chapter:** ف7
- **Page:** ص159–161
- **Example:** (FILM، [EXTERNAL: WEB]) عتمان يُجبر أبو العلا على الطلاق **بالتهديد بتلفيق تهمة سرقة والسجن** (FILM §3.4) — تخويف مخطط لا انفجار.
- **Application:** يفرّق في الحلقة بين «شخص عصبي» (مشكلة تنظيم — المراحل 2–3) و«تخويف محسوب» (مشكلة سيطرة — المرحلة 7): **الهدوء المصاحب للتهديد علامة، لا طمأنة**. [SAFETY]: التهديد الجسدي أو القانوني ⇒ توثيق + جهة رسمية + دعم (KB-120).
- **Related Concepts:** KB-107, KB-120, KB-131, KB-128
- **Potential Visual:** رسم نبض ينخفض بينما يرتفع خط «التهديد» — مفارقة بصرية.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE] + [SAFETY]؛ الربط بعتمان = [INTEGRATED SYNTHESIS]
- **CT#:** 165

### KB-100 · إسكات التعاطف بالتبرير | Silencing Empathy by Self-Justification
- **Definition:** Goleman: المعتدون يبررون أفعالهم «بالكذب على أنفسهم»، ويرون الضحية «من خلال عيني خياله… وليس من خلال التعاطف مع مشاعر» الضحية الحقيقية؛ والندم ينبع من التعاطف (ص157–159). ومعتقدات تبرير العنف: «الناس الذين نضربهم… لا يقاسون كثيرًا»، «إذا تجنبت الضرب، سيعتقد الجميع أنك جبان» (ص326). NVC: «All violence is the result of people tricking themselves… that their pain derives from other people and… deserve to be punished» (L2810). CC: «once demonized, we can abuse» (قصص الشرير، p.109).
- **Book:** Goleman · NVC · CC
- **Chapter:** Goleman ف7، ف15؛ NVC Ch.10؛ CC Ch.6
- **Page:** Goleman ص157–159، ص326؛ NVC L2810؛ CC p.109
- **Example:** (FILM) الشيخ **يعترض أولًا** على عقد الزواج لمخالفة العدة، ثم يمتثل بعد «البلد بلدنا والدفاتر دفاترنا»، وهو يتلو «وأطيعوا الله وأطيعوا الرسول وأولي الأمر منكم» (FILM §3.5) — ضمير يُسكَت بالتبرير [INTEGRATED SYNTHESIS؛ الصياغة الحرفية تُراجع بالمشاهدة].
- **Application:** الكشف: جمل التبرير الجاهزة («هو اللي جابه لنفسه»، «ده لمصلحتها»، «كلنا بنعمل كده»). وتنبيه ذاتي أخلاقي: نفس الآلية قد تعمل عندنا (CC: نحكي قصة الشرير لنبرر أذانا).
- **Related Concepts:** KB-047, KB-106, KB-110, KB-131
- **Potential Visual:** صوت الضمير (خط رفيع) يغطيه ضجيج كلمات تبرير.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [SAFETY] (لا تُعرض أمثلة Goleman عن الاعتداء على الأطفال)؛ الربط بالفيلم = [INTEGRATED SYNTHESIS]
- **CT#:** 164

### KB-101 · المتلوّنون اجتماعيًا — والاستقامة العاطفية | Social Chameleons & Emotional Integrity
- **Definition:** مارك سنايدر (كما يعرضه Goleman): «المتلونون اجتماعيًا» — «متقلبون يغيرون وجوههم وفقًا لمصلحتهم»؛ «مثل الحرباء يظهر للناس بالمظهر الذي يريدونه»؛ علامته: انطباع ممتاز + عجز عن صلات مستقرة؛ «لا يهم المتلونين… أن يقولوا شيئًا ويفعلوا شيئًا آخر». المهارات الاجتماعية إذا لم تتوازن «بإحساس ذكي باحتياجات ومشاعر الآخرين… قد تؤدي إلى مجرد نجاح مزيف». **النموذج الصحي**: من «يوازن بين الصدق مع النفس والمهارات الاجتماعية التي يستخدمها بأمانة وتكامل».
- **Book:** Goleman
- **Chapter:** ف8
- **Page:** ص175–177
- **Example:** (FILM، [EXTERNAL: WEB]) العطار الذي يزيّن رغبة العمدة: «دي بِت ولّادة؛ جابت اتنين في بطن» (FILM §4) — المحيطون الذين يعكسون ما يريده صاحب السلطة [INTEGRATED SYNTHESIS].
- **Application:** **الحد الأخلاقي الفاصل بين EQ وDark EQ من Goleman نفسه: الأمانة + التكامل.** وأساس بند الدرع 1 «الأفعال قبل الكلمات»: التناقض المتكرر بين القول والفعل.
- **Related Concepts:** KB-059, KB-097, KB-132
- **Potential Visual:** حرباء تغير لونها مع كل خلفية ← مقابل شجرة ثابتة الجذع تتحرك أغصانها.
- **Potential Exercise:** جزء من **Exercise 8**: «قال إيه… عمل إيه؟» (عمودين لآخر 3 مواقف مع شخص يربكك).
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]
- **CT#:** 168

### KB-102 · من يمسك «إيقاع» الجماعة | Controlling the Emotional Tempo
- **Definition:** Goleman: في التفاعل «الإنسان المسيطر يتحدث أكثر… بينما يظل الطرف الآخر… ينظر إلى وجه الطرف الأول»؛ قوة «السياسي أو المبشر» تصل إلى مشاعر الجماهير و«تضعهم في قبضة يده»؛ «فالجذب العاطفي هو جوهر التأثير». الإيقاع (Zeitgeber) — من يضبط الحالة الانفعالية للمجموعة (ص170–173).
- **Book:** Goleman
- **Chapter:** ف8
- **Page:** ص168–173
- **Example:** (إيجابي) الرهبان الذين أطفأوا رغبة القتال (ص168)؛ (سلبي — [INTEGRATED SYNTHESIS]) مجلس يحدد فيه صاحب السلطة مزاج الحضور، فيضحكون حين يضحك ويصمتون حين يغضب.
- **Application:** يشرح «الضغط الاجتماعي» في تحليل عتمان (POWER · SOCIAL PRESSURE) وفي مكان العمل (الاجتماع الذي يُحسم بمزاج المدير). **الحماية**: لاحظ إن كان مزاجك في الغرفة «مستعارًا» — KZ: «just because other people's minds are waving about, it doesn't mean that [yours] have to too» (KB-129).
- **Related Concepts:** KB-069, KB-107, KB-108, KB-129
- **Potential Visual:** مايسترو في المنتصف وأمواج مزاج تتبع عصاه؛ شخص واحد يلاحظ ويخرج من الإيقاع.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]؛ التطبيق = [INTEGRATED SYNTHESIS]
- **CT#:** 167

### KB-103 · الذنب كأداة | Guilt-Tripping
- **Definition:** NVC: «The basic mechanism of motivating by guilt is to attribute the responsibility for one's own feelings to others» (مثال: «It hurts Mommy and Daddy…»)؛ «Where guilt is a tactic of manipulation and coercion, it is useful to confuse stimulus and cause… To motivate by guilt, mix up stimulus and cause»؛ وثقافة «uses guilt as a means of controlling people» (L2740–2744). اختبار المطالبة: إن رُفضت فجاء **لوم أو ذنب** ⇒ كانت مطالبة (L1761–1797). MoM — الرد: «Acknowledge any truth in someone's complaints about you, and at the same time stand up for your own rights»: «I understand you are disappointed, and yet I need to say no… That is not being selfish; it is just taking care of myself» (p.262). وأسئلة تقييم خطورة الفعل: هل يعتبره الآخرون خطيرًا؟ كيف سيبدو بعد 5 سنوات؟ (p.269–271).
- **Book:** NVC · MoM
- **Chapter:** NVC Ch.5، Ch.6، Ch.10؛ MoM Ch.15
- **Page:** NVC L1209، L1761–1797، L2740–2744؛ MoM p.262، p.269–271
- **Example:** مثال الـBrief (تعليمي): «لو كنت بتحترمني كنت وافقت» ← فكرة تلقائية «أنا شخص سيئ» ← ذنب ← امتثال. ثم: الحقيقة (طلب + لوم عند الرفض) ← فكرة بديلة («الرفض مش قلة احترام؛ الضغط بالذنب علامة إنه مطالبة») ← شعور أهدأ ← حد. بنية المثال تطابق مثال NVC «If you really loved me, you'd…».
- **Application:** **Dark EQ + MoM** و**Dark EQ + NVC** في الـBrief. صيغة الحد (الـBrief): «لما يتم ربط الطلب بإحساسي بالذنب، أنا مش مرتاح للطريقة دي. أنا مستعد أتكلم عن المشكلة نفسها، لكن مش هقدر أوافق تحت ضغط». **توازن**: ليس كل ذنب مصطنعًا — «A responsibility pie is not designed to always reduce guilt. Sometimes it is healthy to feel guilty» (MoM p.274؛ KB-119).
- **Related Concepts:** KB-039, KB-074, KB-078, KB-119, KB-052
- **Potential Visual:** حبل مربوط بين «طلب» و«إحساسك بالذنب» — مقص يقطعه ويترك «الطلب» وحده للنقاش.
- **Potential Exercise:** **Exercise 8 (أ)**: «جملة الذنب»: المشاهد يكتب الفكرة التلقائية ← الدليل ← الفكرة البديلة ← جملة الحد.
- **Tag:** [DIRECT SOURCE] (NVC + MoM)؛ مثال الـBrief = [USER-PROVIDED FRAMEWORK]؛ الربط = [INTEGRATED SYNTHESIS]
- **CT#:** 52, 57, 140

### KB-104 · سحب الاهتمام والصمت العقابي | Withdrawal & Punitive Silence
- **Definition:** NVC: القوة العقابية تشمل «withholding gratification»، و**«the withdrawal of caring or respect is one of the most powerful threats of all»** (L3400–3402). CC: يوتام يعترف: «I pout because I'm hurting. And I also do it hoping it'll make you feel bad» (p.88–90)، وإيفون تمتثل ثم تستاء (p.65–66). Goleman: «تجميد المناقشة» = «التباعد والتعالي والنفور» (ص196–197).
- **Book:** NVC · CC · Goleman
- **Chapter:** NVC Ch.12؛ CC Ch.5؛ Goleman ف9
- **Page:** NVC L3400–3402؛ CC p.65–66، p.88–90؛ Goleman ص196–197
- **Example:** (علاقات) «مش هكلمك» كلما رُفض طلب، ويعود الدفء فورًا عند الموافقة.
- **Application:** بند **Withdrawal** في «Dark EQ في العلاقات». **التمييز الإلزامي**: الانسحاب بسبب «الطوفان» حماية ذاتية مشروعة (KB-092) ≠ الانسحاب **المشروط** المتكرر كوسيلة ضغط. العلامة: الدفء يعود مقابل التنازل لا مقابل الحوار.
- **Related Concepts:** KB-092, KB-093, KB-094, KB-118
- **Potential Visual:** منظم حرارة (ترموستات) للدفء في يد طرف واحد، يرفع ويخفض مع كل «نعم/لا».
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ التطبيق = [INTEGRATED SYNTHESIS]
- **CT#:** 69

### KB-105 · المديح المتلاعب | Manipulative Praise
- **Definition:** NVC: المديح «positive judgment»؛ مدراء استخدموه لأنه يرفع الإنتاجية، فانخفضت الإنتاجية حين «sense the manipulation behind the appreciation»؛ **«Express appreciation to celebrate, not to manipulate»** (L3670–3680).
- **Book:** NVC
- **Chapter:** Ch.14
- **Page:** L3670–3680
- **Example:** (عمل) مديح مبالغ فيه يسبق طلبًا غير معقول مباشرة، ويتكرر بالتوقيت نفسه.
- **Application:** أقرب سند مصدري لما يسميه الـBrief «Love bombing» — **المصطلح نفسه غير موجود في المصادر** ⇒ [NOT SUPPORTED BY PROVIDED SOURCE] كمصطلح؛ نصفه كسلوك: «اهتمام/مديح مكثف يُستخدم مقدمة لطلب أو سيطرة». كيف تتعرف: المديح عام («انت أحسن واحد») لا محدد (فعل + احتياج + شعور — KB-080)، ويأتي مقرونًا بطلب.
- **Related Concepts:** KB-080, KB-094, KB-111
- **Potential Visual:** باقة ورد يخرج منها خيط مربوط بطلب.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ «Love bombing» = [USER-PROVIDED FRAMEWORK] + [NOT SUPPORTED BY PROVIDED SOURCE] كمصطلح
- **CT#:** 71

### KB-106 · لغة السلطة وإنكار المسؤولية | Language of Authority & Denial of Responsibility
- **Definition:** NVC: إنكار المسؤولية عبر «dictates of authority»، ضغط الجماعة، السياسات، الأدوار — «Amtssprache» (لغة المكاتب عند أيخمان)؛ المطالبات «common… among those who hold positions of authority»؛ لغة المجتمعات المهيمنة: «When we are in contact with our feelings and needs, we humans no longer make good slaves and underlings» (L742). «The most dangerous of all behaviors may consist of doing things 'because we're supposed to'» (L2708). «the use of vague and abstract language can mask oppressive interpersonal games» (L1619).
- **Book:** NVC
- **Chapter:** Ch.2، Ch.6، Ch.9، Ch.13
- **Page:** L666–742، L1619، L2674–2708، L3512
- **Example:** (FILM، [EXTERNAL: WEB]) «البلد بلدنا والدفاتر دفاترنا، اكتب يا شيخ…» — السلطة تجعل الإجراء الرسمي أداة، والمنفذ يكتب «لأن الأمر صدر» (FILM §3.5، §4) [INTEGRATED SYNTHESIS]. (عمل) «إحنا عيلة واحدة» لطلب معلومة شخصية أو ساعات بلا أجر (مثال الـBrief).
- **Application:** يفسر كيف ينفّذ «الأتباع» ما يرفضه ضميرهم (الشيخ، الخفير). **كيف تحمي نفسك**: ترجم الجملة من لغة «لازم/الأوامر» إلى «مين طلب إيه بالضبط؟» + وثّق (KB-091).
- **Related Concepts:** KB-073, KB-100, KB-107, KB-131
- **Potential Visual:** ختم رسمي كبير يُطبع فوق وجه إنسان فيخفيه.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ الربط بالفيلم وبمثال الـBrief = [INTEGRATED SYNTHESIS]
- **CT#:** 46, 47

### KB-107 · السلطة المُرهِبة تُسكت الجميع | Intimidating Authority Silences the Room
- **Definition:** Goleman: الطيار (1978) «مستبد يرهب من يعملون معه»؛ مساعدوه «خافوا من ثورة غضبه، لم يتدخلوا بالرأي حتى عندما كانت الكارثة وشيكة» ← تحطم الطائرة (ص213–214)؛ «الضغط العصبي يصيب الناس بالغباء»؛ «القيادة… لا تعني السيطرة». قد يكون المدير خبيرًا لكن ضعف ثقة الناس به «يقوض قدرتهما على الإدارة» (ص232–235). CC: الناس يصمتون «rather than anger someone in power» (p.22)؛ القادة يسببون الخوف وينكرونه ← «ghosts of previous leaders» (p.198–200). NVC: التعاطف مع الأقوى أصعب (L2365).
- **Book:** Goleman · CC · NVC
- **Chapter:** Goleman ف10؛ CC Ch.2، Ch.11؛ NVC Ch.8
- **Page:** Goleman ص213–215، ص232–235؛ CC p.22، p.198–200؛ NVC L2365–2367
- **Example:** مريض اللوزتين الذي أُجريت له عملية في قدمه وسكت 7 أشخاص (CC p.22).
- **Application:** عنصر **POWER** في تحليل عتمان، و«Dark EQ in Workplace». **الحماية**: CC — اشتغل على نفسك أولًا، استشر زميلًا، STATE بالحقائق؛ KZ: لا تتنازل عن سلطتك الداخلية (KB-112).
- **Related Concepts:** KB-083, KB-102, KB-108, KB-112, KB-131
- **Potential Visual:** قمرة قيادة: قائد بوجه أحمر، ومساعد يرى إنذارًا ولا يتكلم.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]؛ الربط بعتمان = [INTEGRATED SYNTHESIS]
- **CT#:** 175, 37, 62

### KB-108 · صمت الشهود قبول ضمني | Silent Bystanders Legitimize
- **Definition:** Goleman: «غض النظر عن أفعال التعصب… يسمح بازدهار» التمييز؛ «عدم اتخاذ أي إجراء… هو في حد ذاته فعل له نتائجه»؛ «ومجرد تسمية هذا السلوك علنيًا باسمه… ومعارضته… يخلق مناخًا يحجم فيه»؛ صمت الكبار «رسالة ضمنية بقبول» (ص225–227). و«الغضب التعاطفي» — جون ستيوارت ميل «حارس العدل»؛ كلما زاد التعاطف مع الضحية زاد احتمال تدخل المارة (ص156–157).
- **Book:** Goleman
- **Chapter:** ف7، ف10
- **Page:** ص156–157، ص225–227
- **Example:** (FILM) صمت أهل القرية وخوفهم (FILM §7 — يُصاغ كنمط درامي مع التحقق من مشاهد محددة) [INTEGRATED SYNTHESIS].
- **Application:** عنصر **SOCIAL PRESSURE** في تحليل عتمان، ودرس للمشاهد كـ«شاهد» لا كضحية فقط: تسمية السلوك بهدوء (لا مهاجمة الشخص) تغيّر المناخ. [SAFETY]: التدخل لا يعني تعريض النفس للخطر.
- **Related Concepts:** KB-102, KB-107, KB-116, KB-131
- **Potential Visual:** دائرة وجوه صامتة؛ صوت واحد يقول جملة وصفية فتتغير ألوان الوجوه.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]؛ الربط بالفيلم = [INTEGRATED SYNTHESIS]
- **CT#:** 177

### KB-109 · العقاب حسب مزاج صاحب السلطة | Punishment by the Powerful Person's Mood
- **Definition:** Goleman: في الأسر التي تنتج عدوانية، العقاب «ليس بسبب ما يفعلونه، إنما نتيجة لحالة الأبوين المزاجية» ← الطفل يشعر «بعدم قيمته، وعجزه… وأنه سيواجه التهديدات في كل مكان»؛ «حياة الأسرة مدرسة للعدوانية»، والآباء «ليس بالضرورة أن يكونوا أشرارًا… هم ببساطة يكررون النموذج الأبوي» (ص274–275). MoM: «Anxiety is often triggered in vague and ambiguous situations» (p.233).
- **Book:** Goleman · MoM
- **Chapter:** Goleman ف12؛ MoM Ch.14
- **Page:** Goleman ص274–275؛ MoM p.233
- **Example:** (عمل) مدير يعاقب على الخطأ نفسه أحيانًا ويتجاهله أحيانًا حسب يومه ← الفريق يقضي وقته في «قراءة المزاج» بدل العمل.
- **Application:** علامة في «Dark EQ in Workplace»: **عدم القابلية للتنبؤ** يولد خوفًا واعتمادية (FEAR · DEPENDENCY). الحماية: قواعد مكتوبة، توثيق، تثبيت الحقائق (KB-091). وتوازن: Goleman نفسه يقول إنهم «ليسوا بالضرورة أشرارًا» ⇒ نصف السلوك لا الشخص.
- **Related Concepts:** KB-014, KB-091, KB-111, KB-128
- **Potential Visual:** إشارة مرور تتغير عشوائيًا؛ السائقون متجمدون.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]؛ التطبيق على العمل = [INTEGRATED SYNTHESIS]
- **CT#:** 181

### KB-110 · الغطاء الأخلاقي أو الديني للأذى | Moral/Spiritual Cloak for Harm
- **Definition:** KZ: «you have to be on the lookout for tendencies toward self-deception, deluded thinking, grandiosity, self-inflation, and impulses toward exploitation and cruelty directed at other beings. A lot of harm has come in all eras from people attached to one view of spiritual 'truth.' And a lot more has come from people who hide behind the cloak of spirituality and are willing to harm others to feed their own appetites» (PDF p.172).
- **Book:** KZ
- **Chapter:** «Is Mindfulness Spiritual?»
- **Page:** PDF p.172
- **Example:** (FILM، [EXTERNAL: WEB]) توظيف آية «وأطيعوا الله وأطيعوا الرسول وأولي الأمر منكم» لإسكات اعتراض على عقد يخالف العدة (FILM §3.5). وتشير مقالة رأي (الجزيرة 2024) إلى «فتوى أهم» في الفيلم تقر ببطلان الطلاق المكره — تفاصيلها تُراجع بالمشاهدة (FILM §3.6).
- **Application:** عنصر «الخطاب الأخلاقي أو الديني داخل القصة» في تحليل عتمان (مطلب الـBrief). **صياغة إلزامية**: النقد موجه **لتوظيف** الرموز المقدسة لإسكات الناس، **لا للدين** — والفيلم نفسه (حسب المصادر) يحمل داخل القصة موقفًا دينيًا مضادًا للإكراه. الحماية: السؤال «هل الرمز هنا بيحميني ولا بيسكتني؟» + رأي خارجي موثوق (الدرع بند 6).
- **Related Concepts:** KB-100, KB-106, KB-131
- **Potential Visual:** عباءة تُلقى فوق يد تمسك قيدًا — ثم تُرفع العباءة.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] (KZ)؛ الربط بالفيلم = [INTEGRATED SYNTHESIS] + [EXTERNAL: WEB]
- **CT#:** 102

### KB-111 · خلق الاعتمادية والعطاء غير الواعي | Dependency Creation & Mindless Giving
- **Definition:** KZ: «Mindless giving is never healthy or generous… some kinds of giving are not a display of generosity but rather of fear and lack of confidence»؛ قد تستخدم العطاء «as a way of making sure others like you or feel dependent on you»؛ «Perhaps you need to give less, or to trust your intuition about exploitation or unhealthy motives» (PDF p.54–55). و«Out of fear and yearning for someone special… people sometimes fall into unhealthy dependency relationships with meditation teachers» (p.128). MoM — **كارلا** (إرضاء الآخرين): كانت تعتقد أن الآخرين أهم منها وتتجنب الصراع؛ حين بدأت تؤكد نفسها «certain family members got quite upset… some family members had come to expect that she would always give in» — ثم مع الوقت «others often were willing to compromise» (p.172–173).
- **Book:** KZ · MoM
- **Chapter:** KZ «Generosity»، «Wherever You Go»؛ MoM Ch.12
- **Page:** KZ PDF p.54–55، p.128؛ MoM p.172–173
- **Example:** (عمل) زميل/مدير يحتكر المعلومة أو المهارة لتظل محتاجًا له؛ (علاقات) عزل تدريجي عن الأصدقاء «لأنهم مش فاهمينك زيي».
- **Application:** عنصر **DEPENDENCY** في عتمان (الفقر + الأمية ← الاعتماد على صاحب الأرض والأوراق، FILM §6 — مسموح: «استغل سلطته الاقتصادية على فلاحين فقراء وأميين»). **درس كارلا**: من اعتاد تنازلك قد يغضب من حدودك — **مقاومة التغيير متوقعة وليست دليلًا على أنك مخطئ**.
- **Related Concepts:** KB-112, KB-122, KB-051, KB-131
- **Potential Visual:** شجرة صغيرة مربوطة بعصا دعم لم تُفك أبدًا — الجذور لم تنمُ.
- **Potential Exercise:** «في علاقة معينة: لو قلت لأ مرة، إيه اللي بتتوقع يحصل؟ وإيه اللي حصل فعلًا آخر مرة؟» (تجربة سلوكية صغيرة — KB-051).
- **Tag:** [DIRECT SOURCE] (KZ + MoM)؛ التعميم من سياق المعلم الروحي = [INTEGRATED SYNTHESIS]
- **CT#:** 82, 93, 129

### KB-112 · لا تتنازل عن سلطتك الداخلية | Your Own Authority
- **Definition:** KZ: رموز السلطة (المعاطف البيضاء) وإسقاطات «Dr. Have-it-all-together»؛ الهدف «to challenge and encourage people to become their own authorities… each person is already the world authority on him- or herself»؛ «being a little more assertive, for asking more questions»؛ تدني تقدير الذات «a wrong calculation, a misperception» — «projecting onto others that they are okay and we are not»؛ **«Why should they give away their power?»** (PDF p.124–125). و«Dignity»: «We were helped to feel unworthy… coming back to our original worthiness» (p.79).
- **Book:** KZ
- **Chapter:** «Your Own Authority»؛ «Dignity»
- **Page:** PDF p.79، p.124–125
- **Example:** المرضى الذين يتعلمون السؤال بدل الصمت أمام الطبيب. Goleman يعيش العكس: عجز عن سؤال أخصائي الكلى فسأل صديقه نيابة عنه (ص257–258).
- **Application:** بند حماية أمام **POWER · STATUS**: «احترام السلطة ≠ تسليم عقلك لها». وضعية «الكرامة» (KZ) قبل أي محادثة حدود.
- **Related Concepts:** KB-107, KB-111, KB-129
- **Potential Visual:** شخص صغير أمام ظل ضخم على الحائط؛ الإضاءة تتغير فيتضح أن الظل مجرد ظل.
- **Potential Exercise:** «اقف أو اقعد بكرامة 30 ثانية» (KZ TRY، p.79) قبل مكالمة صعبة.
- **Tag:** [DIRECT SOURCE]
- **CT#:** 92, 86

### KB-113 · رؤية النية السلبية مهارة صحية | Recognizing Negative Intent Is Healthy
- **Definition:** MoM: «positive core beliefs can be problems if we lose the flexibility to perceive negative aspects of ourselves, others, and the world. For example, **if somebody is trying to take advantage of you, it is helpful to be able to recognize this person's negative intention**. It is helpful to be aware that some dogs do bite» (p.158). CC: «Sometimes the stories we tell are accurate. The other person is trying to cause us harm… It's not common, but it can happen» (p.109). KZ: الثقة «if not based on naivete» (p.52)، و«trust your intuition about exploitation» (p.55)؛ وأمير «The Water of Life» «pays a high price for his naivete» (p.70).
- **Book:** MoM · CC · KZ
- **Chapter:** MoM Ch.12؛ CC Ch.6؛ KZ «Trust»، «Generosity»، «Practice as a Path»
- **Page:** MoM p.158؛ CC p.109؛ KZ PDF p.52، p.55، p.70
- **Example:** —
- **Application:** **المبرر المصدري لوجود موديول Dark EQ من داخل الكتب نفسها** (خصوصًا من العلاج المعرفي). جملة للحلقة: «مش كل الناس بتعض… بس فيه كلاب بتعض فعلًا — والمهارة إنك تفرّق».
- **Related Concepts:** KB-114, KB-047, KB-123
- **Potential Visual:** رادار يلتقط إشارة حقيقية وسط إشارات كاذبة.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] (3 كتب)؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 128, 81

### KB-114 · معايرة الرادار: لا سذاجة ولا بارانويا | Calibrate the Radar
- **Definition:** MoM: من نشأ في بيئة مؤذية قد يكون من التكيف «to view others as dangerous and to remain constantly alert»، لكن نفس المعتقد يعوق الثقة بأشخاص غير مؤذين و«at risk of misinterpreting everyday behaviors as negative and aggressive» (p.155)؛ «you may have developed a very fine ability to spot and respond to dangerous situations… it may be important to evaluate whether or not you are overresponding» (p.230). الحل: «the mental flexibility to draw on the core belief that was most accurate and adaptive for the person she was with at any given time ("People are dangerous," "People are kind")» (p.155). NVC: كلمة «manipulated» تفسير لا شعور (L1047–1063)؛ MoM: «I've been taken advantage of» = Thought (Worksheet 6.1، p.47–49). KZ: شعر هو نفسه بأنه «manipulated» من صديقة ابنته المتأخرة — «eddy of self-righteous indignation» — ففاته وجه ابنته (p.158).
- **Book:** MoM · NVC · KZ
- **Chapter:** MoM Ch.6، Ch.12، Ch.14؛ NVC Ch.4؛ KZ «Anger»
- **Page:** MoM p.47–49، p.155، p.230؛ NVC L1047–1063؛ KZ PDF p.158
- **Example:** KZ (p.158): حادثة يومية شعر فيها «بالاستغلال» تبيّن أنها قصة نابعة من «I» لا يريد الانتظار.
- **Application:** **البند التوازني الأهم في الدرع**: «افحص قصتك قبل ما تحكم» — «حاسس إني مستغَل» = فرضية تُختبر بالحقائق والنمط (KB-043، KB-094)، **لا تُنكر ولا تُصدَّق تلقائيًا**. يمنع تحويل الموديول إلى «شك في الكل».
- **Related Concepts:** KB-036, KB-043, KB-057, KB-094, KB-113
- **Potential Visual:** مقبض حساسية على رادار — طرف «يرن على كل حاجة» وطرف «مطفي» والمنتصف «مضبوط».
- **Potential Exercise:** **Exercise 8 (ب)**: «المستغل ولا سوء فهم؟» — 4 مواقف: المشاهد يفصل الحقائق عن التفسير ويحدد: واقعة/نمط.
- **Tag:** [DIRECT SOURCE] (3 كتب) + [SAFETY]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 127, 49, 98

### KB-115 · الإساءة لا تُعالج بتغيير الأفكار | Abuse Is Not Solved by Reframing
- **Definition:** MoM: «Some life situations are so challenging that simply thinking differently about things is not a wise idea… someone who is being abused needs help either to change or to leave the situation. Just changing thoughts is not an adequate solution for abuse: The goal is to stop the abuse… simply changing thoughts to permit acceptance of abuse is not a helpful solution» (p.24). و«WHAT IF YOUR HOT THOUGHT IS SUPPORTED BY THE EVIDENCE?» — «one of our hot thoughts may be "My boss is abusing me," and this may be accurate»؛ وحينها «it alerts us that this is something we need to manage or change» (p.112–113). وتغيير البيئة: «learning to say no to unreasonable demands… taking action to reduce discrimination or harassment on the job» (p.24).
- **Book:** MoM
- **Chapter:** Ch.3، Ch.9
- **Page:** p.24، p.112–113
- **Example:** —
- **Application:** **حد أخلاقي يُقال صراحة مرتين**: في نهاية المرحلة 3 («أدوات REFRAME مش عشان تقنع نفسك تستحمل الإساءة») وفي افتتاح المرحلة 7. يحسم جزءًا من **[BOOK DIFFERENCE D4]**.
- **Related Concepts:** KB-045, KB-054, KB-117, KB-120
- **Potential Visual:** نظارة «إعادة التأطير» تُخلع أمام لافتة «خطر» حمراء — الأداة لا تُستخدم هنا.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [SAFETY]
- **CT#:** 106, 120

### KB-116 · غياب الغضب أمام الإساءة مشكلة أيضًا | Absent Anger in the Face of Abuse
- **Definition:** MoM: «People who believe they are helpless often react to abuse not with anger, but with resignation or depression. If you feel helpless in the face of abuse, your challenge may be learning to experience anger when someone is hurting you, rather than learning to control it. Therefore, anger can be a problem either because it is too frequent… or because it is absent. It is normal to feel angry sometimes, and anger can be a healthy and adaptive response» (p.256). و«If we rarely experience anger, and angry thoughts arise from a clear injustice, our response will be to find out how to use our anger to respond constructively» (p.258). Goleman: «الغضب التعاطفي» — «حارس العدل» (ص156).
- **Book:** MoM · Goleman
- **Chapter:** MoM Ch.15؛ Goleman ف7
- **Page:** MoM p.256، p.258؛ Goleman ص156
- **Example:** (FILM — [INTEGRATED SYNTHESIS]) أهل القرية ≈ نموذج «العجز ← الاستسلام بدل الغضب» في مواجهة سلطة لا تُقاوَم.
- **Application:** يكمل تحدي أرسطو (KB-002): الغضب «من الشخص المناسب وبالقدر المناسب». **[BOOK DIFFERENCE D3]**: NVC «We are never angry because of what others say or do» مقابل MoM «anger can be a healthy and adaptive response» للإساءة — كلاهما يرى الغضب إشارة؛ يختلفان في مصدره وقيمته.
- **Related Concepts:** KB-002, KB-039, KB-053, KB-108
- **Potential Visual:** جرس إنذار مكتوم بقطعة قماش — تُرفع القطعة فيرن بصوت منضبط.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [BOOK DIFFERENCE D3]؛ الربط بالفيلم = [INTEGRATED SYNTHESIS]
- **CT#:** 136

### KB-117 · المسامحة ليست إلزامية — ولست مذنبًا — والمسافة مشروعة | No Forced Forgiveness; Not to Blame; Distance
- **Definition:** MoM: «forgiveness is about relieving ourselves of the burden of anger. It does not mean overlooking the actions of the other person» (p.263). و**«Sometimes we may decide not to forgive someone, such as when someone continues abusing us… the only way to let go of anger may be to accept that the other person is abusive, be clear in our own minds that we are not to blame, and figure out ways to protect ourselves from future abuse. Action Plans… can help us design a series of actions and responses to protect ourselves from abuse. Sometimes this includes putting distance between ourselves and the abusive person»** (p.263). KZ يشترط في إرسال الطيبة للوالدين/الصعبين «If you feel capable of it and it feels healthy to you» (p.109).
- **Book:** MoM · KZ
- **Chapter:** MoM Ch.15؛ KZ «Loving Kindness Meditation»
- **Page:** MoM p.263–265؛ KZ PDF p.107–110
- **Example:** —
- **Application:** يحسم **[BOOK DIFFERENCE D4]** (التعاطف مع المسيء مقابل الحدود) و**D5** (الابتعاد كحماية). يُقال في الدرع: «التعاطف قيمة، بس مش واجب على حساب سلامتك».
- **Related Concepts:** KB-115, KB-118, KB-120, KB-092
- **Potential Visual:** مسافة تُرسم على الأرض بخط واضح؛ الشخص يقف خلفها هادئًا.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [SAFETY]
- **CT#:** 141, 90

### KB-118 · القوة الحامية مقابل القوة العقابية — واختبار النية | Protective vs. Punitive Force; the Two Questions
- **Definition:** NVC: قد لا تتاح فرصة الحوار — الطرف الآخر لا يريد التواصل أو هناك خطر وشيك — فيلزم استخدام القوة «to protect life or individual rights». **القوة الحامية** تمنع الأذى أو الظلم؛ **العقابية** تهدف لإيلام المخطئ (ومنها سحب الاهتمام). **السؤالان**: «What do I want this person to do?» و«What do I want this person's reasons to be for doing it?». وNVC «ليست تساهلًا» (غرفة «افعل لا شيء» في المدرسة البديلة).
- **Book:** NVC
- **Chapter:** Ch.12 «The Protective Use of Force»
- **Page:** L3370–3424
- **Example:** إمساك طفل يجري نحو الشارع — قوة حامية لا عقابية (L3378–3382).
- **Application:** **اختبار أخلاقي للمشاهد نفسه** في ختام Dark EQ: «عايز الشخص يعمل إيه؟ وعايزه يعمله ليه — عشان مقتنع ولا عشان خايف؟» — إن كانت الإجابة الثانية فأنت تقترب من المسار الأحمر (KB-097). ويؤكد أن الحدود (القوة الحامية) مشروعة داخل NVC نفسه.
- **Related Concepts:** KB-074, KB-097, KB-117, KB-122
- **Potential Visual:** يدان: واحدة تمسك يد طفل عند الرصيف (حماية)، وأخرى تشير بإصبع اتهام (عقاب).
- **Potential Exercise:** «اختبار السؤالين» على موقف كنت عايز فيه حد يوافق.
- **Tag:** [DIRECT SOURCE]؛ استخدامه كاختبار أخلاقي = [INTEGRATED SYNTHESIS]
- **CT#:** 68, 69

### KB-119 · لوم الذات وفطيرة المسؤولية | Self-Blame & the Responsibility Pie
- **Definition:** MoM: «Young children tend to believe that everything that happens is their responsibility… many abused children decide that the abuse is their fault» (p.155). **فطيرة المسؤولية**: اكتب كل الأطراف والظروف، و«Draw your own slice last, so that you do not prematurely assign too much responsibility to yourself»؛ و**«A responsibility pie is not designed to always reduce guilt. Sometimes it is healthy to feel guilty»** (p.272–274). سؤال الدليل: «Am I blaming myself for something over which I do not have complete control?» (p.75). Goleman: أفضل برامج الحماية تعلّم الأطفال ألا «يلوموا» أنفسهم إذا حدث لهم شيء (ص353).
- **Book:** MoM · Goleman
- **Chapter:** MoM Ch.8، Ch.12، Ch.15؛ Goleman ف15
- **Page:** MoM p.75، p.155، p.272–274؛ Goleman ص353
- **Example:** فيك: رسم فطيرته فوجد أغلب المسؤولية عليه (وقف قريبًا وصرخ في وجهها) ← إصلاح وتغيير (p.273–274) — الأداة لا تمنح المخطئ عذرًا.
- **Application:** أداة مزدوجة في الدرع: **تحرر من تعرض للتلاعب من اللوم الزائف، ولا تعطي المتلاعب مخرجًا**. [SAFETY]: لا نستخدم مثال ماريسا (الاعتداء) في الفيديو.
- **Related Concepts:** KB-044, KB-103, KB-056, KB-121
- **Potential Visual:** دائرة مقسمة لشرائح ملونة؛ شريحة «أنا» تُرسم في النهاية.
- **Potential Exercise:** ارسم فطيرة مسؤولية لموقف تلوم نفسك عليه — شريحتك آخر واحدة.
- **Tag:** [DIRECT SOURCE] + [SAFETY]
- **CT#:** 142

### KB-120 · العجز مقابل استعادة السيطرة — وشبكة الدعم | Helplessness vs. Regaining Control; Support Network
- **Definition:** Goleman (شارني): الكلمة الحاسمة في الصدمة «غير المحكومة» — «الناس الذين يبذلون أي جهد للتحكم بعض الشيء في موقف مفجع… أكثر نجاحًا عاطفيًا… من الذين يشعرون بالعجز التام» (ص283–284). **إيرين**: بعد مطاردة وتهديدات لم تأخذها الشرطة بجدية في البداية، «استطاعت تعبئة أصدقائها وأسرتها لعمل عازل بينها وبين الشخص الذي يطاردها، واستطاعت أيضًا أن تقنع الشرطة بالتدخل»؛ مراحل هيرمان للتعافي: الأمان ← التذكر والحزن ← بناء حياة (ص291–293). MoM: خطة العمل أعادت لماريسا «feel in control again» (p.121)؛ اختيار «relationships and environments… more consistently supportive» (p.163)؛ القلق يتضمن «Underestimating help available» (p.224)؛ و«If you are being physically or sexually abused, almost all communities have special programs nearby to help you» (p.201). Goleman: العزلة خطر، والوحدة = «غياب الإنسان الذي يمكن أن نلجأ إليه» (ص253–255).
- **Book:** Goleman · MoM
- **Chapter:** Goleman ف11، ف13؛ MoM Ch.10، Ch.12، Ch.13، Ch.14
- **Page:** Goleman ص253–255، ص283–284، ص291–293؛ MoM p.121، p.163، p.201، p.224
- **Example:** إيرين (Goleman ص291–293).
- **Application:** **أساس بنود الدرع 5 و6 و«SUPPORT»** في «HOW TO BREAK THE LOOP» (AWARENESS ← BOUNDARIES ← FACTS ← CALM RESPONSE ← DOCUMENTATION ← SUPPORT). حيلة فاطمة في الفيلم **حل درامي في عجز كامل** — لا تُقدَّم كنموذج واقعي (FILM §6)؛ النموذج الواقعي = دعم + جهة رسمية + متخصص. [EXTERNAL]: موارد مساعدة مصرية تُتحقق قبل ذكرها.
- **Related Concepts:** KB-117, KB-121, KB-126, KB-131
- **Potential Visual:** شخص وحيد في دائرة ← تظهر حوله دوائر: صديق، أسرة، جهة رسمية، متخصص — تكوّن «عازلًا».
- **Potential Exercise:** «خريطة الدعم»: اكتب 3 أسماء تلجأ لها لو اتلخبطت (الدرع بند 6).
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE] + [SAFETY]؛ الربط بالدرع = [INTEGRATED SYNTHESIS]
- **CT#:** 182, 183, 131, 179

### KB-121 · المعلومات وحدها لا تحمي | Information Alone Does Not Protect
- **Definition:** Goleman: في برامج الوقاية، المعلومات الأساسية وحدها «لا قيمة لها»؛ البرامج الشاملة ذات الكفاءات العاطفية والاجتماعية جعلت الأطفال أقدر على «أن يطلبوا من المعتدين تركهم وشأنهم، وأن يستغيثوا… ويهددوهم بالإبلاغ… بل يبلغوا عنهم بالفعل». «ليس كافيًا أن يعرف الطفل الفرق…» بل يحتاج **الوعي بالذات، والثقة بالنفس، واتخاذ الفعل المناسب** — «حتى لو كان في مواجهة… بالغ يحاول أن يؤكد… أن ما يفعله… أمر لا غبار عليه». أفضل البرامج تعلّم «الدفاع عما يريدون وتأكيد حقوقهم… ومعرفة حدودهم والدفاع عنها… ولا يلومونها [أنفسهم]… وأن وراءهم مجموعة تساندهم» (ص351–353).
- **Book:** Goleman
- **Chapter:** ف15
- **Page:** ص351–353
- **Example:** — ([SAFETY]: يُذكر المبدأ فقط؛ لا تُعرض تفاصيل برامج الاعتداء)
- **Application:** **أقوى أساس مصدري للدرع كله** + تبرير تصميم الموديول: معرفة التكتيكات لا تكفي ⇒ لذلك الموديول يدرّب على مهارات (وعي + حد + فعل + دعم + عدم لوم الذات)، **لا على قائمة «حيل»**. وعبارة «أن ما يفعله… لا غبار عليه» = تطبيع/إعادة تعريف الواقع كتكتيك يُتعرّف عليه.
- **Related Concepts:** KB-119, KB-120, KB-122, KB-097
- **Potential Visual:** كتاب «معلومات» مغلق ← بجانبه درع يُبنى من 5 قطع: وعي، ثقة، حد، فعل، دعم.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [SAFETY]
- **CT#:** 186

### KB-122 · الحدود ليست عدوانًا — مراحل التحرر العاطفي | Boundaries Are Not Aggression
- **Definition:** NVC — ثلاث مراحل: (1) **العبودية العاطفية** (نظن أننا مسؤولون عن مشاعر الآخرين) (2) **المرحلة «البغيضة»** (الغضب والرفض الحاد لتلك المسؤولية) (3) **التحرر العاطفي**: «respond to the needs of others out of compassion, never out of fear, guilt, or shame»، و«we can never meet our own needs at the expense of others» (L1441–1483). وNVC ≠ التساهل (L3424). KZ: «A non-judging orientation certainly does not mean that you cease knowing how to act or behave responsibly in society, or that anything anybody does is okay» (p.51)؛ و«I practice saying no to keep my life simple» (p.58–59).
- **Book:** NVC · KZ
- **Chapter:** NVC Ch.5، Ch.12؛ KZ «Non-Judging»، «Voluntary Simplicity»
- **Page:** NVC L1441–1483، L3424؛ KZ PDF p.51، p.58–59
- **Example:** —
- **Application:** الأساس المصدري لجملة الـBrief **«الحدود ليست عدوانًا»**: المرحلة الثانية (البغيضة) تحذير من أن تتحول الحدود إلى هجوم؛ الهدف المرحلة الثالثة.
- **Related Concepts:** KB-078, KB-095, KB-118, KB-123
- **Potential Visual:** ثلاث درجات: شخص يحمل الجميع على كتفه ← شخص يرمي الأحمال بعنف ← شخص يقف معتدلًا ويمد يده باختياره.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ الربط بجملة الـBrief = [INTEGRATED SYNTHESIS]
- **CT#:** 55, 80

### KB-123 · الثقة بالدرجات — لا ثقة عمياء ولا عداء شامل | Trust in Degrees
- **Definition:** CC: الثقة «in degrees»، ومرتبطة بالموضوع؛ نوعان: **الدافع** و**القدرة**؛ «Deal with trust around the issue, not around the person»؛ «If they play games, call them on it»؛ ولا تستخدم عدم الثقة كهراوة (p.200–201). KZ: الثقة «if not based on naivete» (p.52).
- **Book:** CC · KZ
- **Chapter:** CC Ch.11؛ KZ «Trust»
- **Page:** CC p.200–201؛ KZ PDF p.52
- **Example:** «أثق في زميلي في الشغل الفني… لكن مش في المواعيد» — ثقة موضوعية.
- **Application:** يعالج «ONE INCIDENT» دون هدم العلاقة كلها؛ ويقابل «فرط اليقظة» (KB-114).
- **Related Concepts:** KB-094, KB-113, KB-114
- **Potential Visual:** لوحة مفاتيح إضاءة (Dimmer) لكل موضوع بدل مفتاح واحد On/Off.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]
- **CT#:** 38

### KB-124 · الامتثال تحت الضغط ليس موافقة | Compliance Under Pressure ≠ Agreement
- **Definition:** CC يقتبس Samuel Butler: «He that complies against his will is of his own opinion still» (p.23). NVC: الامتثال خوفًا أو ذنبًا أو خجلًا يولد الاستياء ويخفض تقدير الذات ويكلّف حسن النية (L640–642)؛ و«If a worker's performance is prompted by fear of punishment, the job gets done, but morale suffers» (L3406–3408)؛ «winning through fear/guilt/shame now → pay later» (L2830–2832). CC: إيفون تمتثل ثم تستاء (p.65–66)؛ و«false dialogue… calmly arguing our side until the other person gives in» (p.83).
- **Book:** CC · NVC
- **Chapter:** CC Ch.2، Ch.5؛ NVC Ch.2، Ch.10، Ch.12
- **Page:** CC p.23، p.65–66، p.83؛ NVC L640–642، L2830–2832، L3406–3408
- **Example:** (FILM، [EXTERNAL: WEB]) طلاق تحت التهديد (FILM §3.4) — إكراه لا موافقة؛ وتشير مقالة رأي إلى موقف داخل الفيلم ببطلان الطلاق المكره (يُراجع بالمشاهدة).
- **Application:** للمشاهد وللمتلاعب معًا: «اللي خد "نعم" بالضغط ما خدش اقتناع». يدعم بند الدرع 2.
- **Related Concepts:** KB-065, KB-074, KB-083, KB-131
- **Potential Visual:** رأس يهز «نعم» بينما الظل على الحائط يهز «لا».
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ الربط بالفيلم = [INTEGRATED SYNTHESIS]
- **CT#:** 7 (Butler)، 8

### KB-125 · التجاوز الصريح: خاص، محترم، حازم — ثم التصعيد | Harassment: Private, Respectful, Firm — then Escalate
- **Definition:** CC: «a vast majority of these problems go away if they're privately, respectfully, and firmly discussed»؛ STATE بالحقائق؛ **«if the behavior is over the line, you shouldn't hesitate to contact HR to ensure your rights and dignity are protected»** (p.194–195). وصف السلوك بدقة أقوى من الاتهام العام (p.126).
- **Book:** CC
- **Chapter:** Ch.7، Ch.11
- **Page:** p.126، p.194–195
- **Example:** —
- **Application:** الخطوة الأخيرة في سلسلة الـBrief «DOCUMENT / ESCALATE WHEN NECESSARY» — المصدر المباشر للتصعيد المؤسسي. [SAFETY]: التحرش والتهديد ⇒ لا تكتفِ بمهارات الحوار.
- **Related Concepts:** KB-091, KB-095, KB-120
- **Potential Visual:** سلم من 3 درجات: حديث خاص ← توثيق ← جهة رسمية.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [SAFETY]
- **CT#:** 36

### KB-126 · الإفصاح الانتقائي الآمن — وكسر صمت الخزي | Safe Selective Disclosure; Breaking Shame's Silence
- **Definition:** MoM: ماريسا فكرت فيما يمكن قوله **بأمان** للمشرف («she wasn't sure it was safe») ← «under a lot of stress… working hard to straighten things out» (p.120–121). والخزي تحيط به السرية («a family secret… considered dishonorable in the community»، p.267)؛ **كسر صمت الخزي**: «It is not unusual for people who have carried a secret for a lifetime to be surprised at the acceptance they receive» — اختر أكثر الناس ثقة وتوقيتًا مناسبًا (p.276–277).
- **Book:** MoM
- **Chapter:** Ch.10، Ch.15
- **Page:** p.120–121، p.267، p.276–277
- **Example:** بيترا تفصح تدريجيًا لصديقتها مونيك فيزداد القرب (p.276–277).
- **Application:** أساس بند الدرع 3 **«لا تقدم معلومات شخصية حساسة بلا داعٍ»** (الإفصاح الانتقائي — [INTEGRATED SYNTHESIS]) مع توازنه: **شارك مع الآمن** لأن السر المحبوس قد يصبح أداة في يد من يعرفه («Using private information as pressure» في الـBrief).
- **Related Concepts:** KB-120, KB-111
- **Potential Visual:** خزنة: مفتاح يُعطى لشخص واحد موثوق — لا تُترك مفتوحة لكل الغرفة.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ التطبيق على الدرع = [INTEGRATED SYNTHESIS]
- **CT#:** 144

### KB-127 · ألعاب الكلام | Word Games
- **Definition:** CC: «silver-tongued individuals» يتلاعبون بالألفاظ ويجدون ثغرات؛ الحل: تحدث عن **النمط** والسلوكيات والنتائج لا عن التعريفات (p.211–212). NVC: «the use of vague and abstract language can mask oppressive interpersonal games» (L1619). CC «dirty tricks» في الإقناع: تكديس الأدلة، المبالغة، الألفاظ الملتهبة، الاحتماء بالسلطة («that's what the boss thinks»)، مهاجمة الشخص، التعميم المتسرع (p.136–138) — يعرضها CC كإفراط منّا نحن في الدفاع عن آرائنا.
- **Book:** CC · NVC
- **Chapter:** CC Ch.7، Ch.11؛ NVC Ch.6
- **Page:** CC p.136–138، p.211–212؛ NVC L1619
- **Example:** «أنا ما قلتش إنك لازم تيجي الجمعة… قلت إنه يفضّل» — بعد أن عومل الغياب كتقصير.
- **Application:** «Blame shifting» و«إعادة تعريف ما قيل» في الـBrief — نصفها كسلوك ونربطها بالتوثيق (KB-091): المكتوب يُنهي لعبة الألفاظ. ومرآة أخلاقية: CC يقول إننا نحن أيضًا نستخدم هذه «الحيل» حين نتحمس.
- **Related Concepts:** KB-091, KB-094, KB-106
- **Potential Visual:** كلمات تتبدل على السبورة؛ ورقة مكتوبة سابقًا تُرفع كمرجع.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ ربطها بمصطلحات الـBrief = [INTEGRATED SYNTHESIS]
- **CT#:** 42

### KB-128 · لا تشخّص — صف السلوك | Replace Diagnosis with Description
- **Definition:** NVC: التشخيص شكل من أشكال الحكم (L628)؛ روزنبرج يستبدل التشخيص («chronic schizophrenic») بالتواصل مع المشاعر والاحتياجات (L3564–3598). Goleman: رغم وصفه فئات إكلينيكية كالسيكوباتية (ص159–160) يحذر: لا «علامة بيولوجية» للجريمة ومعظم من لديهم نقص تعاطف لا ينحرفون (ص161 حاشية)؛ ويعترف أن صوره عن «عالي IQ/عالي EQ» «مبالغ فيها» (ص69–70). MoM: مقاييسه «not used to diagnose» (p.190، p.220).
- **Book:** NVC · Goleman · MoM
- **Chapter:** NVC Ch.2، Ch.13؛ Goleman ف3، ف7؛ MoM Ch.13–14
- **Page:** NVC L628، L3564–3598؛ Goleman ص69–70، ص159–161؛ MoM p.190، p.220
- **Example:** بدل «هو نرجسي» ← «لما بيتقال له لأ، بيرفع صوته ويهدد بالانسحاب — ودي تالت مرة الشهر ده».
- **Application:** قاعدة الـBrief **«هذا سلوك تلاعبي» بدل «هذا الشخص مريض نفسيًا»** — مدعومة بثلاثة كتب. وتنطبق على عتمان: شخصية درامية، نصف أفعالها.
- **Related Concepts:** KB-073, KB-094, KB-131
- **Potential Visual:** ملصق «تشخيص» يُنزع من ظهر شخص ويُستبدل ببطاقة «سلوك + تكرار + أثر».
- **Potential Exercise:** جزء من **Exercise 8**: حوّل 3 ملصقات إلى أوصاف سلوكية.
- **Tag:** [DIRECT SOURCE]؛ الربط بقاعدة الـBrief = [INTEGRATED SYNTHESIS]
- **CT#:** 70

### KB-129 · لا تدخل لعبة الانفعال — اختبار «أهيمسا» | Don't Enter the Emotional Game; Ahimsa
- **Definition:** KZ عن الأطفال: «just because other people's minds are waving about, it doesn't mean that theirs have to too» (p.168). **Ahimsa**: «It is easy to relate with ahimsa to someone who doesn't threaten you. The test is in how you will relate to a person or situation when you do feel threatened»؛ «The willingness to harm or hurt comes ultimately out of fear»؛ «Without a daily embodiment in practice, lofty ideals tend to succumb to self-interest» (p.143–144). وما ينقله KZ عن الدالاي لاما: «should I let them take my mind as well?» (p.45). Goleman: «التوافق مع الآخرين يتطلب قليلًا من الهدوء النفسي» (ص167).
- **Book:** KZ · Goleman
- **Chapter:** KZ «Parenting Two»، «Non-Harming—Ahimsa»، «Patience»؛ Goleman ف8
- **Page:** KZ PDF p.45، p.143–144، p.168؛ Goleman ص167
- **Example:** الاستفزاز المقصود في اجتماع: رد هادئ واحد بالحقيقة ثم العودة للموضوع (MoM التوكيدي «let's get back to the real issue»، p.261).
- **Application:** بند الدرع 7 + **Dark EQ + Mindfulness** (TRIGGER ← PAUSE ← AWARENESS ← CHOICE ← ACTION) — مع تنبيه الـBrief: المساحة بين المثير والاستجابة تُقدَّم كمبدأ ممارسة (KZ p.64 «automatic reacting → conscious responding») لا كادعاء علمي مطلق.
- **Related Concepts:** KB-022, KB-027, KB-031, KB-102
- **Potential Visual:** بحر هائج حول جبل ثابت (استعارة جبل KZ، p.91–94: الطقس على الجبل = مشاعرنا).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ الربط بـDark EQ = [INTEGRATED SYNTHESIS]
- **CT#:** 101, 95

### KB-130 · تسلسلات الـBrief: من المثير إلى الحد | Brief Sequences Mapped to Sources
- **Definition:** الـBrief يطلب 3 تسلسلات؛ هذا المدخل يربط كل خطوة بمصدرها:
  - **Dark EQ + KZ**: TRIGGER (KB-033) ← PAUSE (KB-022) ← AWARENESS (KB-018/KB-027) ← CHOICE (KB-029) ← ACTION (KZ p.20–21 «move… with resolution»).
  - **Dark EQ + MoM**: EVENT ← AUTOMATIC THOUGHT (KB-041) ← EMOTION ← BEHAVIOR ⇒ FACT (KB-043) ← ALTERNATIVE THOUGHT (KB-045) ← CALMER EMOTION (KB-037) ← BOUNDARY (KB-078).
  - **Dark EQ + CC**: STOP (KB-022) ← OBSERVE (KB-024) ← SEPARATE FACTS FROM INTERPRETATION (KB-043) ← CONTROL EMOTION (KB-092) ← STATE FACTS (KB-089) ← STATE BOUNDARY (KB-095) ← ASK CLEAR QUESTION (KB-064/Goleman ص216) ← DOCUMENT / ESCALATE (KB-091/KB-125).
- **Book:** إطار الـBrief + الكتب الخمسة
- **Chapter:** —
- **Page:** انظر المداخل المرتبطة
- **Example:** تطبيق على مثال الـBrief «لو كنت بتحترمني كنت وافقت» (KB-103).
- **Application:** يجعل تسلسلات الـBrief **مدعومة خطوة بخطوة** دون ادعاء أن مؤلفًا واحدًا وضعها.
- **Related Concepts:** KB-103, KB-131, KB-132
- **Potential Visual:** ثلاث سكك قطار متوازية تتلاقى في محطة «الحد الهادئ».
- **Potential Exercise:** —
- **Tag:** [USER-PROVIDED FRAMEWORK] + [INTEGRATED SYNTHESIS]
- **CT#:** —

### KB-131 · حالة «العمدة عتمان» | The Attaman Case (Fictional/Dramatic)
- **Definition:** شخصية درامية في فيلم «الزوجة الثانية» (1967، إخراج صلاح أبو سيف، أداء صلاح منصور). **المدعوم بالمصادر [EXTERNAL: WEB]**: جمع الأراضي بالاحتيال واستغلال فلاحين فقراء وأميين؛ أجبر أبو العلا على تطليق فاطمة بالتهديد بتلفيق تهمة سرقة والسجن؛ سخّر الشيخ لإضفاء شرعية دينية وتجاوز اعتراضه بـ«البلد بلدنا والدفاتر دفاترنا»؛ الحافز المعلن: الرغبة في وريث؛ النهاية: سكتة/شلل ثم وفاة، وتعاد الأراضي وتُتلف الأوراق المزورة (FILM §3، §6). **الممنوع**: التشخيص، اختراع دوافع داخلية، مشاهد أو جمل غير متحقق منها (⚠️ في FILM §4)، ربطه بأشخاص حقيقيين، تقديم حيلة فاطمة كنموذج واقعي.
- **Book:** FILM (+ ربط بالكتب)
- **Chapter:** —
- **Page:** FILM_notes §1–§8
- **Example:** تحليل الـBrief الثماني — الربط المصدري (كلها [INTEGRATED SYNTHESIS]):
  - **POWER** ← Goleman ص213–214 (KB-107)؛ «البلد بلدنا والدفاتر دفاترنا» (KB-106).
  - **FEAR** ← تهديد بتلفيق تهمة (KB-099)؛ Goleman ص160–161.
  - **STATUS** ← مكانة العمدة وسلطة الأوراق؛ CC «We borrow power from the boss» (KB-084).
  - **GUILT/RELIGIOUS FRAME** ← توظيف الآية (KB-110، KB-100).
  - **DEPENDENCY** ← فقر وأمية الفلاحين (KB-111).
  - **SOCIAL PRESSURE** ← صمت القرية (KB-108، KB-102).
  - **AUTHORITY** ← الشيخ ينفّذ بعد اعتراض (KB-106).
  - **EMOTIONAL NEEDS** ← المعلن فقط: الرغبة في وريث ذكر — **لا نضيف دوافع نفسية غير معروضة**. قراءة KZ «what looks like strength is often… an attempt to cover up fear» (p.56) تُذكر إن استُخدمت كـ**عدسة تفسيرية موسومة** لا كحقيقة عن الشخصية.
  - **«الأبوة الزائفة»** (مطلب الـBrief «إذا كان المصدر يدعمها») ⇒ **[NOT SUPPORTED BY PROVIDED SOURCE]** حتى الآن — لا يوجد في مصادر الويب ما يثبت خطاب «أبوي» لعتمان؛ يُتحقق بالمشاهدة قبل الاستخدام.
- **Application:** Case Study رئيسية في Dark EQ + **Recurring Visual Character** عند: Power (KB-107)، Fear (KB-099)، Empathy vs Exploitation (KB-097)، Boundaries (KB-122) — دون إفراط.
- **Related Concepts:** KB-097 → KB-129, KB-132
- **Potential Visual:** Animation 9 «تشريح المتلاعب»: شخصية مرسومة (غير مطابقة لصورة الممثل — [EXTERNAL KNOWLEDGE]: تجنب حقوق الصورة) في المنتصف، حولها 7 كلمات (POWER · FEAR · STATUS · GUILT · DEPENDENCY · SOCIAL PRESSURE · EMOTIONAL NEEDS) ← «HOW THE SYSTEM WORKS» ← «HOW TO BREAK THE LOOP».
- **Potential Exercise:** **Exercise 8 (ج)**: «لو كنت واحد من أهل القرية… أنهي خطوة من الدرع كانت ممكنة؟» (بدون تشجيع مخاطرة واقعية).
- **Tag:** [EXTERNAL: WEB] + [INTEGRATED SYNTHESIS] + قيود [NOT SUPPORTED BY PROVIDED SOURCE]
- **CT#:** 189

### KB-132 · درع Dark EQ — الأساس المصدري لكل بند | Dark EQ Shield — Source Basis
- **Definition:** الدرع [USER-PROVIDED FRAMEWORK] — بنوده السبعة مع أقوى سند لكل بند:
  1. **الأفعال قبل الكلمات** ← Goleman ص145–146 (الحقيقة في الكيف) + ص175–177 (المتلونون «يقولون شيئًا ويفعلون شيئًا آخر») + KZ p.64 («do you manifest it or just talk a lot?») + CC p.114 (ركّز على أثر الأفعال) — KB-059، KB-101.
  2. **لا تتخذ قرارًا تحت الخوف أو الذنب** ← Goleman ص48–49، ص118 (تجمد الذاكرة العاملة) + NVC L1209، L2740 (الذنب أداة) + MoM p.262 — مع توازن KB-011 (الإحساس معلومة) — KB-010، KB-103.
  3. **لا تقدم معلومات شخصية حساسة بلا داعٍ** ← MoM p.120–121 (الإفصاح الآمن) — التطبيق [INTEGRATED SYNTHESIS] — KB-126.
  4. **ضع حدودًا واضحة** ← MoM p.261–263 (التوكيد) + CC p.208–209 + NVC Ch.12 + KZ p.51 — KB-078، KB-095، KB-118، KB-122.
  5. **وثّق الأمور المهمة** ← CC p.177 («One dull pencil…») + p.192 — التطبيق [INTEGRATED SYNTHESIS] — KB-091.
  6. **اطلب رأيًا خارجيًا عند التشوش** ← Goleman ص291–293 (إيرين)، ص353 + MoM p.201، p.224 + CC p.199 (استشر زميلًا) — KB-120.
  7. **لا تدخل في لعبة الانفعال** ← KZ p.168 + p.45 + Goleman ص167 — KB-129.
  - **«الهدوء ليس استسلامًا»** ← KZ p.23 + MoM p.127–128 — KB-054.
  - **«الحدود ليست عدوانًا»** ← NVC L1441–1483، L3424 + KZ p.51 — KB-122.
- **Book:** إطار الـBrief + الكتب الخمسة
- **Chapter:** —
- **Page:** انظر أعلاه
- **Example:** —
- **Application:** Animation 10 «Dark EQ Shield» + ملف `14_DARK_EQ_SHIELD.md` (المرحلة 8).
- **Related Concepts:** KB-097 → KB-131
- **Potential Visual:** درع من 7 قطع يتجمع قطعة قطعة، وكل قطعة تحمل أيقونة البند.
- **Potential Exercise:** **Exercise 8** (نسخة كاملة): «درعك الشخصي» — أضعف بند عندك وخطوة واحدة لتقويته.
- **Tag:** [USER-PROVIDED FRAMEWORK] + [INTEGRATED SYNTHESIS]
- **CT#:** —

---

# المرحلة 8 — INTEGRATE | اجمع كل المهارات
*العمود الفقري: Goleman القسم الرابع «الفرص المتاحة» (ف12–14) + القسم الخامس «محو الأمية العاطفية» (ف15–16) + الكلمة الأخيرة. داعم: MoM ف16 · KZ · CC ف12.*

### KB-133 · مراحل اكتساب المهارة الثلاث — وخطة الانتكاس | Three Stages of Skill; Relapse Plan
- **Definition:** MoM: (1) واعية ومكتوبة (2) في الذهن بجهد واعٍ (3) تلقائية — «"I'm such a failure"… "Wait a minute. I messed this up, but that doesn't make me a failure"… later… simply think, "Oh, I messed this up"». «Often when we start to feel better, we stop using the skills… It is actually better to keep deliberately using helpful skills until they become automatic». **خطة تقليل الانتكاس**: المواقف عالية الخطورة ← علامات الإنذار المبكر («try asking family members or friends») ← خطة عمل. «Experiencing a variety and intensity of moods is a normal and valuable part of life»؛ الانتكاس «an opportunity to strengthen your skills».
- **Book:** MoM
- **Chapter:** Ch.16 «Maintaining Your Gains»
- **Page:** p.280–289
- **Example:** بن: سجلات أفكار إذا تجاوزت الدرجة 15 + يوميات امتنان أسبوعية + تقدير شخص واحد أسبوعيًا (p.285–288). ماريسا: موقفها عالي الخطورة «when she thought that people didn't care about her or were taking advantage of her».
- **Application:** بنية «خطتي الشخصية» في آخر الحلقة وفي خطة الأيام السبعة: 7 أيام = **المرحلة 1 (مكتوبة)** فقط — أمانة زمنية.
- **Related Concepts:** KB-017, KB-034, KB-135, KB-142
- **Potential Visual:** سلم من 3 درجات: ورقة وقلم ← فقاعة تفكير ← «أوتوماتيك».
- **Potential Exercise:** «خطتي للانتكاسة»: أخطر موقف عليّ / أول علامة / أول خطوة.
- **Tag:** [DIRECT SOURCE]
- **CT#:** 145

### KB-134 · دروس صغيرة ومتكررة — وإشارات تذكير | Small, Repeated Lessons & Cues
- **Definition:** Goleman: التعلم العاطفي «دروس صغيرة لكنها مؤثرة، تصل إليه بانتظام وعلى مدى سنين… فالخبرات تتكرر مرارًا، يعكسها المخ كمسارات قوية، وعادات عصبية، يستعملها أوقات التهديد والإحباط والإهانة» (ص357–359). CC: أعداء التغيير الثلاثة — المفاجأة، الانفعال («Your ability to pull yourself out of the content… is inversely proportional to your level of emotion»)، والنصوص الجاهزة؛ الحل **الإشارات**: نقطة حمراء على المقود أو الساعة، بطاقات تذكير؛ و«start immediately» بمحادثة متوسطة الخطورة (p.215–226). KZ: 5 دقائق يوميًا قد تكفي، وقرار الممارسة يُتخذ «the night before» (p.85، p.117–119). NVC: بطاقة سام ويليامز 3×5 (L2906–2916).
- **Book:** Goleman · CC · KZ · NVC
- **Chapter:** Goleman ف16؛ CC Ch.12؛ KZ «How Long to Practice?»، «Early Morning»؛ NVC Ch.10
- **Page:** Goleman ص357–359؛ CC p.215–226؛ KZ PDF p.84–85، p.117–119؛ NVC L2906–2916
- **Example:** «Daddy, get the card!» — الطفل يذكّر أباه بالبطاقة (NVC).
- **Application:** تصميم خطة الأيام السبعة: تمرين واحد صغير يوميًا + إشارة تذكير مادية (ستيكر/منبه). [SOURCE LIMITATION]: فصل 16 في الترجمة المرفقة مختصر والملاحق غير موجودة — لا نستشهد بمنهج Self-Science التفصيلي.
- **Related Concepts:** KB-034, KB-133, KB-142
- **Potential Visual:** نقطة حمراء على ساعة اليد تظهر في لقطات متعددة عبر الحلقة (Easter egg بصري).
- **Potential Exercise:** «اختار إشارتك»: ستيكر أحمر على الموبايل = «نَفَس قبل ما ترد».
- **Tag:** [DIRECT SOURCE] (4 كتب)؛ التصميم = [INTEGRATED SYNTHESIS]
- **CT#:** 43, 174

### KB-135 · مقياس لا أبيض وأسود — التقدم لا الكمال | Rate Progress, Not Pass/Fail
- **Definition:** MoM: فيك قيّم ضبط غضبه **75%** لا «فشل»: رفع صوته وضرب الطاولة مرة، لكنه «did not criticize Judy, leave the house, or behave in any way she considered threatening… took one three-minute timeout» (p.169–171). Figure E.1: درجات بن تذبذبت (ارتفعت في الأسبوع 3) لكن الاتجاه العام هبط (p.292–293)؛ وتقدم فيك «interrupted by two episodes of binge drinking» (p.295). CC: «don't aim for perfection. Aim for progress» (p.91، p.228).
- **Book:** MoM · CC
- **Chapter:** MoM Ch.12، Epilogue؛ CC Ch.5، Ch.12
- **Page:** MoM p.169–171، p.292–296؛ CC p.91، p.228
- **Example:** فيك (p.170).
- **Application:** يوم REFLECT (اليوم 7): «قيّم نفسك بنسبة مش بـ"نجحت/فشلت"». رسم «التحسن مش خط مستقيم».
- **Related Concepts:** KB-017, KB-133, KB-056
- **Potential Visual:** رسم بياني متعرج يتجه عمومًا للأسفل (شدة الانفعال) — خط اتجاه منقط فوقه.
- **Potential Exercise:** «من 0 لـ100: قد إيه اتحكمت في نفسك في أصعب موقف الأسبوع ده؟ وإيه اللي عملته صح؟»
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 145

### KB-136 · الدافع يأتي بعد الفعل | Motivation Follows Action
- **Definition:** MoM: «motivation often follows doing something rather than coming first, especially when we are depressed»؛ «The goal… is to increase the number and types of activities… not to perfectly complete every activity» (p.216). Goleman (تايس): «انتصار بسيط أو نجاح سهل» من أنجح طرق تحسين المزاج (ص111). CC: «do something» — الفصل يُطبق 3–5 أيام (p.221).
- **Book:** MoM · Goleman · CC
- **Chapter:** MoM Ch.13؛ Goleman ف5؛ CC Ch.12
- **Page:** MoM p.216؛ Goleman ص111؛ CC p.221
- **Example:** بن: الجلوس في الكرسي يوم الثلاثاء (متعة 0) مقابل كرة القدم مع الأحفاد يوم السبت (MoM p.201–204).
- **Application:** جملة ختامية للخطة: «ما تستناش تبقى جاهز… ابدأ بخطوة صغيرة والجاهزية هتيجي بعدها».
- **Related Concepts:** KB-050, KB-133, KB-142
- **Potential Visual:** دومينو: أول قطعة صغيرة تُسقط سلسلة أكبر.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]؛ الالتقاء = [INTEGRATED SYNTHESIS]
- **CT#:** 132

### KB-137 · التدفق — الذكاء العاطفي في أحسن حالاته | Flow
- **Definition:** تشيكسنتميهاي: «التدفق» = «نسيان الذات»، عكس الاجترار والقلق؛ يحدث «في تلك المنطقة الشعورية الدقيقة ما بين الملل والقلق»، والمخ فيه أهدأ وأكفأ؛ «التدفق… الذكاء العاطفي في أحسن حالاته». خلاصة الفصل: التمكن = «توجيه انفعالاتنا إلى غاية مثمرة».
- **Book:** Goleman
- **Chapter:** ف6
- **Page:** ص133–141
- **Example:** الجراح الذي لم ينتبه لسقوط جزء من السقف (ص135–137) [REPORTED IN SOURCE].
- **Application:** الوجه «الإيجابي» للتنظيم العاطفي في الختام: الهدف ليس فقط إطفاء الحرائق بل الوصول لحالة أداء واستمتاع. (يربط بمنحنى U — KB-014.)
- **Related Concepts:** KB-014, KB-017
- **Potential Visual:** قناة بين ضفتين «ملل» و«قلق»؛ القارب يجري في المنتصف.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]
- **CT#:** 159

### KB-138 · الدعم الاجتماعي والكتابة | Social Support & Expressive Writing
- **Definition:** Goleman: العزلة الاجتماعية ترتبط بزيادة خطر المرض [REPORTED IN SOURCE]؛ «الوحدة ليست مثل العزلة» — الخطر في «الإحساس الذاتي بالانقطاع… وغياب الإنسان الذي يمكن أن نلجأ إليه»؛ والعلاقات السلبية لها ضريبتها. بنيبيكر: الكتابة عن أكبر المخاوف/الصدمات لبضعة أيام ارتبطت بمناعة أفضل؛ النموذج الأصح: التعبير عن المشاعر ثم «سرد القصة في نسيج… متكامل» واكتشاف المعنى (ص253–257).
- **Book:** Goleman
- **Chapter:** ف11
- **Page:** ص253–257
- **Example:** —
- **Application:** يوم REFLECT: 10 دقائق كتابة. **[BOOK DIFFERENCE داخلي]**: الكتابة المنظِّمة ≠ «التنفيس» الذي يرفضه Goleman نفسه (ص97–98). **تحفظ علمي**: دراسة شبيجل عن مجموعات الدعم وإطالة العمر [EXTERNAL KNOWLEDGE: لم تتكرر نتيجتها لاحقًا] — لا تُستخدم.
- **Related Concepts:** KB-120, KB-048, KB-135
- **Potential Visual:** دفتر مفتوح تتحول سطوره المتشابكة إلى خط واضح.
- **Potential Exercise:** «اكتب 10 دقايق: إيه اللي حصل، حسيت بإيه، واتعلمت إيه».
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE] + [EXTERNAL KNOWLEDGE] (التحفظ)
- **CT#:** 179

### KB-139 · الطبع ليس قدرًا — والمخ يتعلم مدى الحياة | Temperament Is Not Destiny
- **Definition:** Goleman: «الطبع ليس قدرًا محتومًا»؛ ثلث الأطفال شديدي الاستثارة تخلصوا من الخجل؛ الأمهات اللاتي يضعن حدودًا حازمة ويتركن الطفل يتعلم تهدئة نفسه بـ«جرعات صغيرة» يساعدنه أكثر من الحماية الزائدة؛ «لا يوجد طبع إنساني لا يمكن تغييره»؛ العلاج السلوكي للوسواس غيّر نشاط المخ مثل الدواء — «لقد غيرت خبرتهم وظيفة المخ» (ص307–312)؛ «المخ يظل طيعًا مدى الحياة، ولكن ليس بالقدر المذهل نفسه في سن الطفولة» (ص315). لودو: «إذا تعلمت منظومتك العاطفية شيئًا ما مرة واحدة، فلن يضيع منها أبدًا» — العلاج يعلّم التحكم لا المحو (ص297)؛ لوبورسكي: «الحساسية الكامنة… لم تتغير» بينما تحسنت الاستجابات (ص297–298).
- **Book:** Goleman
- **Chapter:** ف13، ف14
- **Page:** ص297–315
- **Example:** عمة Goleman «جوون» سقطت بعد السكتة فضحكت: «حسن، أخيرًا أستطيع أن أسير مرة أخرى» (ص304–305).
- **Application:** رسالة أمل صادقة في الختام: **«مش هتبقى شخص تاني… هتبقى نفس الشخص بمهارات أكتر»** (الحساسية تبقى، والاستجابة تتغير).
- **Related Concepts:** KB-017, KB-133, KB-001
- **Potential Visual:** مسار في غابة يتكون بخطوات متكررة (مسار عصبي جديد) بجانب المسار القديم الذي يبهت.
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE] + [REPORTED IN SOURCE]؛ رأي ديفيدسون عن رفع نشاط الفص الأيسر «مازال… ينتظر اختبارات» (ص307) — يُذكر بتحفظ Goleman
- **CT#:** 158, 182

### KB-140 · المكونات الفعالة — مخرجات التعلم | Active Ingredients (W.T. Grant)
- **Definition:** Goleman ينقل قائمة «المكونات الإيجابية»: **المهارات العاطفية** — الوعي بالذات، التمييز والتعبير عن المشاعر، التحكم في المشاعر، تأجيل الإشباع، التعامل مع الضغط، **«معرفة الفرق بين المشاعر والأفعال»**؛ **القرار** — التحكم في الاندفاع ← البدائل ← النتائج قبل التصرف؛ **المهارات العلاقاتية** — فهم الإشارات، الاستماع، **«مقاومة المؤثرات السلبية»**، منظور الآخرين، السلوك المقبول (ص353–355). وقائمة 7 أسس للاستعداد للتعلم (الثقة، حب الاستطلاع، القصدية، السيطرة على النفس، العلاقات، التواصل، التعاون، ص269–272).
- **Book:** Goleman
- **Chapter:** ف12، ف15
- **Page:** ص269–272، ص353–355
- **Example:** —
- **Application:** **مخرجات التعلم الرسمية للحلقة** (تُكتب في وصف يوتيوب وفي Master Outline) — تثبت أن تصميم الحلقة بما فيه «مقاومة المؤثرات السلبية» (Dark EQ) له جذر في الكتاب الأساسي.
- **Related Concepts:** KB-001, KB-029, KB-121
- **Potential Visual:** قائمة تحقق (Checklist) تُعلَّم بنودها واحدًا واحدًا في الختام.
- **Potential Exercise:** —
- **Tag:** [REPORTED IN SOURCE] (قائمة مؤسسة W.T. Grant كما ينقلها Goleman)
- **CT#:** 187

### KB-141 · صور الختام: «إن لم يكن الآن فمتى؟» — المحارة — المصعد | Closing Images
- **Definition:** Goleman يختم الكتاب بسؤال: «ألا ينبغي أن ندرس أهم هذه المهارات الأساسية… أكثر من أي وقت مضى؟ وإن لم يكن الآن فمتى إذن؟!» (ص361–362). MoM يفتتح ويختم باستعارة المحارة: «For an oyster, an irritant becomes the seed for something new and beautiful» (p.1) و«transform future irritants into valuable pearls» (p.296)؛ واستعارة المصعد: المهارات «can lift you out of the basement… not just to ground level, but up to the top floor» (p.289–290)؛ وقصة الصياد «I'll teach you how to fish» (p.280). KZ: «Wherever you go, there you are… 'Now what?'» (p.9).
- **Book:** Goleman · MoM · KZ
- **Chapter:** Goleman كلمة أخيرة؛ MoM Ch.1، Ch.16، Epilogue؛ KZ Introduction
- **Page:** Goleman ص361–362؛ MoM p.1، p.280، p.289–290، p.296؛ KZ PDF p.9
- **Example:** —
- **Application:** مواد الدقائق الأخيرة: المحارة كصورة بصرية للختام (الإزعاج ← لؤلؤة)، وسؤال Goleman كجملة أخيرة قبل الـCTA.
- **Related Concepts:** KB-142, KB-002
- **Potential Visual:** حبة رمل تدخل محارة ← لؤلؤة تتكون (Timelapse مرسوم).
- **Potential Exercise:** —
- **Tag:** [DIRECT SOURCE]
- **CT#:** 188

### KB-142 · «نظام الذكاء العاطفي العملي» وخطة الأيام السبعة — الأساس المصدري | The Integrated System & 7-Day Plan — Source Basis
- **Definition:** **إطار تعليمي متكامل (Integrated Teaching Framework) من تصميم الحلقة [USER-PROVIDED FRAMEWORK] — ليس نموذجًا رسميًا لأي مؤلف.** سند كل خطوة:
  - **NOTICE** ← Goleman ف4 (KB-018) + KZ (KB-020، KB-024).
  - **NAME** ← Goleman ص73–74، ص337–341 + MoM p.25–30 + NVC Ch.4 (KB-035–KB-037).
  - **PAUSE** ← KZ p.20–21، p.63–64 + NVC L2836 «Stop. Breathe» + Goleman ص200–208 (KB-022، KB-027، KB-092).
  - **UNDERSTAND** ← MoM Ch.7–9 + CC Ch.6 (KB-041–KB-047) — «افهم قصتك».
  - **REGULATE** ← Goleman ف5 + MoM p.121–124، p.243 (KB-048، KB-092، KB-023).
  - **EMPATHIZE** ← Goleman ف7 + NVC Ch.7–8 + CC Ch.8 (KB-058–KB-066).
  - **COMMUNICATE** ← NVC + MoM p.261–263 + Goleman ص209–211 (KB-072–KB-079).
  - **NAVIGATE** ← CC (KB-082–KB-095) + NVC Ch.11 (KB-096) + درع Dark EQ عند الحاجة (KB-132).
  - **REFLECT** ← MoM Ch.16 + Goleman ص297 (KB-133، KB-135، KB-138).
  - **خطة 7 أيام** (Observe · Name · Pause · Reframe · Empathize · Communicate · Reflect) [USER-PROVIDED FRAMEWORK]: **تمرين عملي من تصميم الحلقة**؛ أساس «الممارسة اليومية القصيرة» مدعوم (KZ p.85؛ MoM p.63، p.2–3؛ Goleman ص211–212، ص357–359)، لكن **الجدول نفسه غير موجود في أي كتاب**، و7 أيام = بداية (MoM: التلقائية بعد 20–40 سجلًا، والمعتقدات الجديدة «months»).
- **Book:** إطار الـBrief + الكتب الخمسة
- **Chapter:** —
- **Page:** انظر أعلاه
- **Example:** —
- **Application:** Animation 11 «Final Integrated System» + المرحلة 4 (`04_INTEGRATED_FRAMEWORK.md`).
- **Related Concepts:** كل المداخل
- **Potential Visual:** 9 محطات على خط واحد تضيء بالتتابع، ويظهر فوق كل محطة شعار الكتاب الذي يغذيها.
- **Potential Exercise:** خطة الأيام السبعة (Handout).
- **Tag:** [USER-PROVIDED FRAMEWORK] + [INTEGRATED SYNTHESIS]
- **CT#:** —

---

## 10. فروق الكتب — مرجع سريع (D1–D7)
*التفاصيل الكاملة في `01_SOURCE_AUDIT.md` §4.1. هنا فقط: أين يظهر كل فرق في قاعدة المعرفة وكيف يُقال في الحلقة.*

| # | الفرق | الأطراف | المداخل | الصياغة في الحلقة |
|---|---|---|---|---|
| D1 | تغيير الفكرة مقابل مراقبتها | MoM ↔ KZ (الفرق **ضاق**: MoM ط2 يتبنى اليقظة صراحة p.129، p.242) | KB-028, KB-023, KB-045 | «الاتنين متفقين إن الفكرة مش حقيقة؛ واحد يقولك افحصها والتاني يقولك سيبها تعدّي». |
| D2 | التسوية | CC (تسوية = «جيد») ↔ NVC («satisfaction instead of compromise») ↔ MoM في المنتصف (p.172–173) | KB-088, KB-096, KB-111 | «الحل الوسط مش عيب… بس ابدأ بالاحتياجات قبل ما تقسم الكعكة». |
| D3 | مصدر الغضب وقيمته | NVC («never angry because of what others say or do») ↔ MoM (الغضب قد يكون «healthy and adaptive»؛ غيابه أمام الإساءة مشكلة p.256) ↔ Goleman («حارس العدل») | KB-039, KB-053, KB-116 | «تفسيرك بيكبّر أو يصغّر الغضب… بس ساعات الغضب هو الإشارة الصح». |
| D4 | التعاطف مع المسيء مقابل الحدود | NVC (التعاطف مع من يهاجمك) + Goleman (قطار طوكيو) ↔ MoM p.24، p.263 + NVC Ch.12 | KB-068, KB-115, KB-117, KB-118 | «التعاطف قيمة… مش واجب على حساب سلامتك». |
| D5 | ترك الموقف | استراحة للعودة (Goleman/MoM/CC) ↔ تجنب يزيد القلق (MoM p.225–228) ↔ ابتعاد عن مسيء كحماية (MoM p.263) | KB-092, KB-014, KB-117 | «فيه 3 أنواع خروج: هرجع — بهرب — بحمي نفسي». |
| D6 | القصة قبل الشعور؟ (**محسوم**) | CC (قصة ← شعور) ↔ Goleman (إنذار قبل التفكير) | KB-006, KB-040 | «طبقتين: إنذار سريع، وقصة بتغذيه أو تطفيه». |
| D7 | مدة التهدئة | Goleman (20 دقيقة على الأقل) ↔ MoM (5 دقائق–24 ساعة) | KB-092 | «على الأقل 20 دقيقة للجسم… وأحيانًا يوم للقرار». |
| + | تفاصيل صغيرة | XYZ (جوتمان/جينوت) ↔ NVC (الشعور الزائف والطلب)؛ KZ (ملاحظة النفس) ↔ MoM (تنفس 4-4) | KB-076, KB-023 | تُقدَّم كـ«نسخة سريعة» و«نسخة أدق». |

---

## 11. التغطية والضبط

### 11.1 إحصاءات
| البند | القيمة |
|---|---|
| عدد المداخل | **142** |
| المراحل الثماني | كلها مغطاة (1: 17 · 2: 17 · 3: 23 · 4: 14 · 5: 10 · 6: 15 · 7: 36 · 8: 10) |
| صفوف `concept_table.csv` (189) المربوطة | **181** مربوطة بعمود CT#؛ الـ8 الباقية مدمجة/مؤجلة بقرار موثق في §11.3 |
| مداخل [USER-PROVIDED FRAMEWORK] | KB-097 (المصطلح)، KB-130، KB-132، KB-142 — كلها مربوطة بسند لكل خطوة |
| مداخل تعتمد على [EXTERNAL: WEB] | KB-131 (الفيلم) + أمثلة موسومة في KB-099، KB-100، KB-101، KB-106، KB-110، KB-124 |
| [NOT SUPPORTED BY PROVIDED SOURCE] صريح | مصطلح «Dark EQ» (KB-097)؛ «Love bombing» كمصطلح (KB-105)؛ «الأبوة الزائفة» عند عتمان (KB-131)؛ ملاحق Goleman وتفاصيل ف16 (KB-134) |
| [EXTERNAL KNOWLEDGE] صريح | «hostile attribution bias» (KB-057)؛ «الفرسان الأربعة» (KB-093)؛ تحفظ دراسة شبيجل (KB-138)؛ حقوق صورة الممثل (KB-131) |

### 11.2 قرارات منهجية اتُّخذت في هذه المرحلة
1. **الترتيب حسب المراحل الثماني** مع ربط كل مرحلة بقسم Goleman المقابل — يحافظ على Goleman كعمود فقري ويجعل القاعدة جاهزة للمرحلتين 3 (Graph) و5 (Structure).
2. **دمج المفاهيم المتطابقة عبر الكتب في مدخل واحد** (مثل KB-043 الحقيقة/التفسير من 3 كتب) بدل تكرارها؛ مع الحفاظ على الاقتباس والصفحة لكل كتاب — هذا هو «المنهج الواحد» المطلوب لا «تلخيص 5 كتب».
3. **Dark EQ مبني من داخل الكتب الخمسة أولًا** (Goleman: 17 موضعًا مباشرًا؛ MoM: 10 مواضع؛ NVC، KZ، CC) — والمصطلح والتكتيكات غير الموجودة موسومة. لم تصل مادة Dark EQ المستقلة من المستخدم؛ إن وصلت تُضاف كمداخل [USER-PROVIDED FRAMEWORK] دون حذف الأساس المصدري.
4. **كل تكتيك في المرحلة 7 موصوف من زاوية الضحية/الشاهد** (كيف يظهر ← كيف تتعرف ← كيف تحمي نفسك) — لا توجد صياغة «كيف تفعلها».
5. **الأمثلة الحساسة مستبعدة** من الاستخدام المرئي: ماريسا (MoM)، ستايرون، روبلز، أمثلة الاعتداء على الأطفال (Goleman ص157–159)، الأدوية، تجارب التنفس السريع — تبقى مبادئها فقط [SAFETY].
6. **حوار الفيلم**: الجمل المسموح استخدامها الآن (✅ في FILM §4) فقط؛ الباقي ينتظر التحقق بالمشاهدة قبل المرحلة 6.

### 11.3 صفوف من جدول المفاهيم لم تحصل على مدخل مستقل (ودُمجت أو أُجّلت)
| CT# | المفهوم | القرار |
|---|---|---|
| 6 | Self-defeating loops (CC p.6–7) | مدمج كمثال في CASE 2 (المرحلة 5 Structure) — مرتبط بـKB-093 |
| 35 | Two levers (CC p.180–181) | يدمج في KB-084/KB-087 عند كتابة Animation 7 |
| 65 | Have to → Choose to (NVC) | اختياري لخطة الأيام السبعة — مرتبط بـKB-106 |
| 83 | Strength as cover for fear (KZ p.56) | عدسة تفسيرية موسومة داخل KB-131 فقط |
| 87 | Mountain / Lake (KZ) | استعارة بصرية داخل KB-129 |
| 100 | Children as possessions (KZ p.167) | مرتبط بـKB-071 وKB-109 (الأسرة) |
| 115 | Vic & Judy full arc (MoM p.69–98) | موزع على KB-042، KB-043، KB-066، KB-092 — ويصبح **Case مرجعية** في المرحلة 5 |
| 134 | Avoidance & safety behaviors (MoM) | داخل KB-014 وD5 |

### 11.4 المدخلات المطلوبة للمرحلة التالية (PHASE 3 — KNOWLEDGE GRAPH)
- حقل **Related Concepts** في كل مدخل = حواف الرسم البياني (Edges).
- حقل **Tag** = لون الحافة/العقدة (Direct / Synthesis / User framework / External).
- السلاسل الثلاث المطلوبة في الـBrief (EMOTION ← … ← CONSEQUENCE؛ AWARENESS ← … ← CHOICE؛ SELF-AWARENESS + EMPATHY + COMMUNICATION + CONFLICT = PRACTICAL EQ) تُبنى من: KB-003/013/038/040 · KB-018/022/027/029 · KB-018/058/072/082.
