"""Arabic translation strings for GEO PDF report."""

STRINGS = {
    # Cover page
    'report_title': 'تقرير تحليل GEO',
    'report_subtitle': 'تدقيق تحسين محركات البحث التوليدية لـ <b>{brand_name}</b>',
    'label_website': 'الموقع الإلكتروني',
    'label_date': 'تاريخ التحليل',
    'label_score': 'نقاط GEO',
    'score_of_100': '/100',

    # Score tiers
    'tier_excellent': 'ممتاز',
    'tier_good': 'جيد',
    'tier_moderate': 'متوسط',
    'tier_below_avg': 'دون المتوسط',
    'tier_needs_attention': 'يحتاج اهتمام',

    # Section headers
    'section_executive_summary': 'الملخص التنفيذي',
    'section_score_breakdown': 'تفصيل نقاط GEO',
    'section_platform_readiness': 'جاهزية منصات الذكاء الاصطناعي',
    'section_crawler_access': 'حالة وصول زواحف الذكاء الاصطناعي',
    'section_findings': 'النتائج الرئيسية',
    'section_action_plan': 'خطة العمل ذات الأولوية',
    'section_methodology': 'الملحق: المنهجية',
    'section_glossary': 'المصطلحات',

    # Table headers
    'col_component': 'المكوّن',
    'col_score': 'النقاط',
    'col_weight': 'الوزن',
    'col_weighted': 'الموزون',
    'col_platform': 'منصة الذكاء الاصطناعي',
    'col_status': 'الحالة',
    'col_crawler': 'الزاحف',
    'col_recommendation': 'التوصية',
    'col_term': 'المصطلح',
    'col_definition': 'التعريف',

    # Score components
    'comp_citability': 'قابلية الاستشهاد والظهور في الذكاء الاصطناعي',
    'comp_brand': 'إشارات سلطة العلامة التجارية',
    'comp_content': 'جودة المحتوى و E-E-A-T',
    'comp_technical': 'الأسس التقنية',
    'comp_schema': 'البيانات المنظمة',
    'comp_platform': 'تحسين المنصات',
    'comp_overall': 'الإجمالي',

    # Chart labels (short)
    'chart_citability': 'الاستشهاد',
    'chart_brand': 'العلامة',
    'chart_content': 'المحتوى',
    'chart_technical': 'التقنية',
    'chart_schema': 'البيانات',
    'chart_platform': 'المنصات',

    # Descriptions
    'platform_desc': 'تعكس هذه النقاط مدى احتمالية استشهاد كل منصة بحث بالذكاء الاصطناعي بمحتواك. تشير النقاط الأقل من 50 إلى عوائق كبيرة أمام الاستشهاد على تلك المنصة.',
    'crawler_desc': 'يمنع حظر زواحف الذكاء الاصطناعي المنصات من الاستشهاد بمحتواك. يوضح الجدول أدناه أي زواحف الذكاء الاصطناعي يمكنها حالياً الوصول إلى موقعك.',

    # Action plan sub-headers
    'quick_wins_title': 'مكاسب سريعة (هذا الأسبوع)',
    'quick_wins_desc': 'تأثير عالٍ، جهد منخفض \u2014 يمكن تنفيذها فوراً.',
    'medium_term_title': 'تحسينات متوسطة المدى (هذا الشهر)',
    'medium_term_desc': 'تأثير كبير، جهد معتدل \u2014 تتطلب تغييرات في المحتوى أو التقنية.',
    'strategic_title': 'مبادرات استراتيجية (هذا الربع)',
    'strategic_desc': 'ميزة تنافسية طويلة المدى \u2014 تتطلب استثماراً مستمراً.',

    # Header/footer
    'header_text': 'تقرير تحليل GEO-SEO',
    'footer_generated': 'تم الإنشاء {date}',
    'footer_page': 'صفحة {page}',
    'footer_confidential': 'سري',

    # Severity labels
    'severity_critical': 'حرج',
    'severity_high': 'عالي',
    'severity_medium': 'متوسط',

    # Fallbacks
    'fallback_exec_summary': 'يقدم هذا التقرير نتائج تدقيق شامل لتحسين محركات البحث التوليدية (GEO) أُجري على <b>{brand_name}</b> ({url}). قيّم التحليل جاهزية الموقع لمحركات البحث المدعومة بالذكاء الاصطناعي بما في ذلك Google AI Overviews و ChatGPT و Perplexity و Gemini و Bing Copilot. نقاط جاهزية GEO الإجمالية هي <b>{geo_score}/100</b>، مما يضع الموقع في فئة <b>{tier}</b>.',
    'fallback_no_crawlers': '<i>قم بتشغيل /geo crawlers لملء هذا القسم ببيانات وصول زواحف الذكاء الاصطناعي.</i>',
    'fallback_no_findings': '<i>قم بتشغيل تدقيق /geo كامل لملء النتائج.</i>',

    # Methodology
    'methodology_text': 'أُجري تدقيق GEO هذا في {date} لتحليل {url}. قيّم التحليل الموقع عبر ستة أبعاد: قابلية الاستشهاد والظهور في الذكاء الاصطناعي (25%)، إشارات سلطة العلامة التجارية (20%)، جودة المحتوى و E-E-A-T (20%)، الأسس التقنية (15%)، البيانات المنظمة (10%)، وتحسين المنصات (10%).',
    'methodology_platforms': '<b>المنصات التي تم تقييمها:</b> Google AI Overviews، ChatGPT Web Search، Perplexity AI، Google Gemini، Bing Copilot',
    'methodology_standards': '<b>المعايير المرجعية:</b> إرشادات مقيّمي جودة بحث Google (ديسمبر 2025)، مواصفات Schema.org، Core Web Vitals (حدود 2026)، معيار llms.txt الناشئ، إطار ترخيص RSL 1.0',

    # Crawler table data
    'status_allowed': 'مسموح',
    'status_blocked': 'محظور',
    'status_unknown': 'غير معروف',
    'rec_keep_allowed': 'إبقاء السماح',
    'rec_unblock': 'إلغاء الحظر للظهور',

    # Disclaimer
    'disclaimer': 'تم إنشاء هذا التقرير بواسطة أداة تحليل GEO-SEO Claude Code. تستند النقاط والتوصيات إلى التحليل الآلي ومعايير الصناعة. يجب التحقق من النتائج من خلال اختبار خاص بكل منصة.',

    # Glossary entries
    'glossary_entries': [
        ['GEO', 'تحسين محركات البحث التوليدية \u2014 تحسين المحتوى للاستشهاد في بحث الذكاء الاصطناعي'],
        ['AIO', 'نظرات عامة بالذكاء الاصطناعي \u2014 مربعات الإجابة المولدة بالذكاء الاصطناعي من Google في نتائج البحث'],
        ['E-E-A-T', 'الخبرة، التخصص، الموثوقية، الجدارة بالثقة'],
        ['SSR', 'العرض من جانب الخادم \u2014 إنشاء HTML على الخادم لوصول الزواحف'],
        ['CWV', 'مؤشرات الويب الأساسية \u2014 مقاييس تجربة الصفحة من Google (LCP, INP, CLS)'],
        ['INP', 'التفاعل حتى الرسم التالي \u2014 مقياس الاستجابة (حل محل FID مارس 2024)'],
        ['JSON-LD', 'ترميز JavaScript للبيانات المترابطة \u2014 تنسيق البيانات المنظمة المفضل'],
        ['sameAs', 'خاصية Schema.org تربط كياناً بملفاته الشخصية على منصات أخرى'],
        ['llms.txt', 'ملف معياري مقترح لتوجيه أنظمة الذكاء الاصطناعي حول محتوى الموقع'],
        ['IndexNow', 'بروتوكول لإخطار محركات البحث فوراً بتغييرات المحتوى'],
    ],

    # Default action plan items
    'default_quick_wins': [
        'السماح لجميع زواحف الذكاء الاصطناعي من المستوى الأول في robots.txt (GPTBot, ClaudeBot, PerplexityBot)',
        'إضافة تواريخ النشر وآخر تحديث لجميع صفحات المحتوى',
        'إضافة أسماء المؤلفين مع بيانات الاعتماد للمقالات والمدونات',
        'إنشاء ملف llms.txt لتوجيه أنظمة الذكاء الاصطناعي إلى محتواك الرئيسي',
        'إضافة خصائص sameAs إلى مخطط المؤسسة للربط بجميع ملفات المنصات',
    ],
    'default_medium_term': [
        'إعادة هيكلة أهم 10 صفحات بعناوين قائمة على الأسئلة وكتل إجابة مباشرة',
        'تنفيذ ترميز شامل لمخطط Organization + Article + Person',
        'تحسين كتل المحتوى لقابلية الاستشهاد بالذكاء الاصطناعي (134-167 كلمة فقرات مستقلة)',
        'ضمان العرض من جانب الخادم لجميع صفحات المحتوى العامة',
        'تنفيذ بروتوكول IndexNow لسرعة فهرسة Bing/Copilot',
    ],
    'default_strategic': [
        'بناء حضور كيان Wikipedia/Wikidata من خلال التغطية الصحفية والشهرة',
        'تطوير استراتيجية مشاركة مجتمع Reddit نشطة في المنتديات ذات الصلة',
        'إنشاء استراتيجية محتوى YouTube متوافقة مع استعلامات البحث بالذكاء الاصطناعي',
        'إنشاء برنامج نشر أبحاث/بيانات أصلية لقابلية استشهاد فريدة',
        'بناء سلطة موضوعية من خلال مجموعات محتوى شاملة',
    ],
}
