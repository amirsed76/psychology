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
    "mental_disorder": "سابقه‌ی کدامیک از بیماری‌های عصبی-روانشناختی زیر را دارید؟"
}

TERM = """
•	باسلام و سپاس از اینکه با شرکت خود در این پژوهش، ما را برای رسیدن به اهداف آن یاری می‌کنید. 
•	این پژوهش مربوط به انجام پایان نامه مقطع کارشناسی ارشد ، تحت نظارت و راهنمایی دکتر ماهگل توکلی (استاد راهنما) و با اجرای علی صدیقین (دانشجوی کارشناسی ارشد رشته روانشناسی شناختی- دانشگاه اصفهان)  است.
•	ما در این پژوهش تلاش کرده ایم، ابتدا ابزاری جهت اندازه گیری حافظه رویدادی طراحی و اجرا، و سپس ویژگی های آن را ارزیابی و بررسی کنیم.
•	فرآیند و شیوه شرکت در این پژوهش به این صورت است که شما در ابتدا پس از وارد کردن اطلاعات هویتی و عصبی-روانشناختی خود، وارد مرحله پاسخ به پرسشنامه حافظه روزمره (ساندرلند و همکاران) می‌شوید. در این پرسشنامه، یک سری سوالات ساده در مورد قدرت حافظه شما در امور روزمره پرسیده می‌شود.
•	پس از پاسخگویی به پرسشنامه وارد مرحله اجرای آزمون و ابزار طراحی شده در این پژوهش می شوید. سادگی استفاده از آن از مهمترین ویژگی های این ابزار است؛ تعدادی تصاویر به شما نمایش داده خواهد شد؛ شما بایستی هر زمانی که تصور کردید تصویر نمایش داده شده قبلاً تکرار شده است، بلافاصله دکمه فاصله را روی صفحه کلید رایانه را فشار دهید، و یا اگر از گوشی های هوشمند و لمسی استفاده می کنید، روی عکس ضربه بزنید.
•	برای بررسی دقیق‌تر این ابزار، بایستی که شما چند روز پس از انجام آزمون، دوباره به همین سایت مراجعه کنید و بار دیگر آزمون را انجام دهید. تاریخ مراجعه بعدی در انتهای آزمون به شما اعلام خواهد شد. 
•	مطمئناً یاری و همکاری شما باعث می شود تا ابزاری دقیق و سریع برای اندازه گیری حافظه رویدادی برای تشخیص قدرت حافظه افراد فراهم آید که برای تشخیص زودهنگام انواع اختلالات و بیماری های مرتبط با حافظه مثل آلزایمر یاری رسان خواهد بود.
•	چنانچه در انجام فرآیند این پژوهش و یا موضوعات مرتبط سوال و یا مشکلی داشتید، لطفاً با شماره 09384917539 تماس حاصل فرمایید.
•	درباره حافظه رویدادی بیشتر بدانید:
حافظه رویدادی یا حافظه رویدادهای ویژه شامل خاطرات ما از تجارب شخصی خودمان است، 'نوعی فیلم ذهنی از آنچه دیده یا شنیده‌ایم'. به سخن دیگر، حافظهٔ رویدادی شامل اتفاقاتی است که در زندگی ما رخ داده‌اند و به زمان و مکان خاصی وابسته هستند. برای نمونه، وقتی به یاد می‌آوریم که در میهمانی شب گذشته چه کسان تازه‌ای را ملاقات کردیم یا مدارک خود را در کدام کشو گذاشته ایم؛ ما در حافظه رویدادی، خاطرات رویدادهای ویژه را به یاد می‌آوریم. هم‌چنین سرنخ‌ها یا نشانه‌های مربوط به زمان و مکان به ما کمک می‌کنند تا اطلاعات را از این بخش حافظه بازیابیم.

"""

HOW_DO_TASK = {
    "gif": settings.MEDIA_URL + "tutorial.gif",
    "text": "تست بسیار ساده است. تعداد 50 تصویر به ترتیب به شما نشان داده می‌شود. اگر تصویری تکراری نمایش داده شد، کلید را بزنید( کلید space یا ضربه در موبایل) . هر تصویر سه ثانیه به شما نمایش داده می‌شود. زمان واکنش شما ثبت خواهد شد."
}

QUESTION_TEXT = "شما با شرکت در این پژوهش علاوه بر اندازه‌گیری قدرت و میزان سلامتی حافظه خود، به ما کمک می‌کنید تا این ابزار ساخته شده برای اندازه‌گیری حافظه را ارزیابی و بررسی کنیم."

TASK_DAY_DURATION = 7

APPRECIATION = "با سپاس از حُسن همکاری و مشارکت شما، در سمت راست صفحه می‌توانید امتیاز کسب شده در آزمون و میانگین زمان واکنش شما به تصاویر تکراری را ملاحظه کنید که نشان دهنده قدرت و سلامت حافظه رویدادی شما است."
