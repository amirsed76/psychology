from django.conf import settings

ANSWERS = {
    1: "نه اصلاً در شش ماه گذشته",
    2: 'یکبار در شش ماه گذشته',
    3: 'بیش از یک بار در شش ماه گذشته ولی کمتر از یک بار در ماه',
    4: 'یک بار در ماه',
    5: 'بیش از ماهی یکبار، ولی کمتر از هفته ای یکبار',
    6: 'یک بار در هفته',
    7: 'بیش از یک بار در هفته، ولی کمتر از روزی یکبار',
    8: 'روزی یکبار',
    9: 'بیش از روزی یکبار'
}

HELTH_QUESTIONS = {
    "get_covid_19": "آیا تاکنون به بیماری کرونا (کووید 19) مبتلا شده‌اید؟",
    "get_drug": "آیا در 1 ماه گذشته، سابقه‌ی مصرف دخانیات یا مشروبات الکلی را داشته‌اید؟",
    "mental_disorder": "سابقه‌ی کدامیک از بیماری‌های عصبی-روانشناختی زیر را دارید؟ (در صورت عدم سابقه یا اطلاع از آن، هیچ گزینه‌ای را انتخاب نکنید)"
}





TERM = """
•باسلام و سپاس از اینکه با شرکت خود در این پژوهش، ما را برای رسیدن به اهداف آن یاری می‌کنید. 
•این پژوهش مربوط به انجام پایان نامه مقطع کارشناسی ارشد رشته علوم شناختی (گرایش روانشناسی شناختی) ، تحت نظارت و راهنمایی دکتر ماهگل توکلی (استاد راهنما) و با اجرای علی صدیقین (دانشجوی کارشناسی ارشد دانشگاه اصفهان) صورت می‌گیرد.
•ما در این پژوهش قصد داریم، ابتدا ابزاری جهت اندازه گیری حافظه رویدادی طراحی، و سپس ویژگی های آن را ارزیابی و بررسی کنیم.
•برای بررسی دقیق‌تر این ابزار، بایستی که شما چند روز پس از انجام آزمون، دوباره به همین سایت مراجعه کنید و بار دیگر آزمون اصلی را انجام دهید. تاریخ مراجعه بعدی در انتهای آزمون به شما اعلام خواهد شد. 
•مطمئناً یاری و همکاری شما باعث می شود تا ابزاری دقیق و سریع برای اندازه گیری حافظه رویدادی افراد فراهم آید که برای تشخیص زودهنگام انواع اختلالات و بیماری های مرتبط با حافظه مثل اختلال شناختی خفیف و یا آلزایمر یاری رسان خواهد بود.
•لطفاً هرگونه سوال، پیشنهاد و یا انتقاد درباره نحوه انجام فرآیند پژوهش و یا موضوعات مرتبط با آن را از طریق شماره تماس 09384917539 با مجری پژوهش (علی صدیقین) درمیان بگذارید.
"""


QUESTION_HELP = """
در این مرحله، شما به پرسشنامه حافظه روزمره (ساندرلند و همکاران) پاسخ می‌دهید. برای پاسخ به هر سوال کافی است روی گزینه مورد نظر کلیک یا ضربه بزنید.
"""




HOW_DO_TASK = {
    "gif": settings.MEDIA_URL + "tutorial.svg",
    "text": """
انجام این آزمون بسیار ساده است. تعدادی تصویر به شما نمایش داده خواهد شد؛ اگر تصویری تکراری مشاهده کردید، بلافاصله دکمه فاصله (روی صفحه کلید رایانه ) را فشار دهید، و یا اگر از گوشی های هوشمند و لمسی استفاده می‌کنید، روی عکس ضربه بزنید.
در ابتدا به صورت آزمایشی 15 تصویر به شما نمایش داده می‌شود. پس از اتمام مرحله آزمایشی و اطمینان از یادگیری نحوه اجرای آزمون، به مرحله اصلی می‌روید که شامل نمایش 50 تصویر است.
    """
}

FIRST_PAGE = "شما با شرکت در این پژوهش علاوه بر اندازه‌گیری قدرت و میزان سلامتی حافظه خود، به ما کمک می‌کنید تا این ابزار ساخته شده برای اندازه‌گیری حافظه را ارزیابی و بررسی کنیم."

TASK_DAY_DURATION = 30

APPRECIATION = """
•با سپاس از شما بخاطر حُسن همکاری و مشارکت در این پژوهش؛ شما می‌توانید امتیاز کسب شده در آزمون و میانگین زمان واکنش شما به تصاویر تکراری را ملاحظه کنید که نشان دهنده قدرت و سلامت حافظه رویدادی شما است.
•درباره حافظه رویدادی بیشتر بدانید:
حافظه رویدادی یا حافظه رویدادهای ویژه شامل خاطرات ما از تجارب شخصی خودمان است، 'نوعی فیلم ذهنی از آنچه دیده یا شنیده‌ایم'. به سخن دیگر، حافظهٔ رویدادی شامل اتفاقاتی است که در زندگی ما رخ داده‌اند و به زمان و مکان خاصی وابسته هستند. برای نمونه، وقتی به یاد می‌آوریم که در میهمانی شب گذشته چه کسان تازه‌ای را ملاقات کردیم یا مدارک خود را در کدام کشو گذاشته ایم؛ ما در حافظه رویدادی، خاطرات رویدادهای ویژه را به یاد می‌آوریم. هم‌چنین سرنخ‌ها یا نشانه‌های مربوط به زمان و مکان به ما کمک می‌کنند تا اطلاعات را از این بخش حافظه بازیابیم.
"""
