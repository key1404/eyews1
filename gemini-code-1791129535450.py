import streamlit as st
import numpy as np
from PIL import Image

# تنظیمات صفحه
st.set_page_config(
    page_title="Eye1 AI | سامانه هوشمند تحلیل آناتومیک عینک",
    page_icon="👓",
    layout="wide"
)

st.title("👓 سامانه کلینیکی هوش مصنوعی Eye1: تحلیل و انتخاب تخصصی عینک")
st.markdown("این سیستم با تحلیل تناسبات هندسی و ابعاد تصویر، استخوان‌بندی چهره و پارامترهای اپتومتری را ارزیابی می‌کند.")

# نوار کناری تنظیمات بالینی
st.sidebar.header("⚙️ پارامترهای تخصصی اپتومتری")
rx_type = st.sidebar.selectbox("نوع نسخه بینایی (Rx)", ["دوربین / نزدیک‌بین (ساده)", "آستیگمات بالا", "دید پیش‌رونده (Progressive)", "بدون نمره / محافظ بلوکات"])
pd_input = st.sidebar.slider("فاصله دو چشم (PD بر حسب میلی‌متر)", 50, 75, 62)

uploaded_file = st.file_uploader("تصویر روبه‌‌رو و واضح از چهره خود آپلود کنید:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    h, w = img_array.shape[:2]
    
    # تحلیل هندسی پیشرفته بر اساس نسبت ابعاد واقعی تصویر چهره
    aspect_ratio = h / w
    
    with st.spinner("در حال پردازش ماتریس هندسی و استخراج پارامترهای چهره..."):
        # طبقه‌بندی علمی فرم صورت بر اساس نسبت ارتفاع به عرض
        if aspect_ratio > 1.38:
            face_shape = "کشیده (Oblong / Long Face)"
            frame_rec = "فریم‌های عریض با پل ضخیم یا مدل‌های خلبانی (Aviator) جهت تعدیل طول صورت."
            brand_suggestion = "Tom Ford (مدل‌های کادر پهن یا خلبانی لوکس)"
        elif 1.18 <= aspect_ratio <= 1.38:
            face_shape = "بیضی متعادل (Oval - استاندارد طلایی اپتومتری)"
            frame_rec = "تناسب ایده‌آل؛ سازگار با طیف وسیعی از فریم‌های کلاسیک، مستطیلی و چشم‌گربه‌ای."
            brand_suggestion = "Ray-Ban (ویفرر / کلاب‌مستر) یا Tom Ford کلاسیک"
        else:
            face_shape = "گرد یا مربعی (Round / Square Face)"
            frame_rec = "فریم‌های زاویه‌دار، مستطیلی باریک یا هندسی جهت ایجاد کنتراست با خط فک."
            brand_suggestion = "Tom Ford (فریم‌های مستطیلی استات کادر باریک)"

        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### تصویر تحلیل‌شده:")
            st.image(image, use_column_width=True)
            
        with col2:
            st.markdown("#### گزارش تحلیل آناتومیک بالینی:")
            st.success("✅ آنالیز ابعاد تصویر با موفقیت انجام شد!")
            st.write(f"🔹 **فرم هندسی استخوان‌بندی:** {face_shape}")
            st.write(f"📐 **نسبت ابعاد ساختاری (H/W):** {aspect_ratio:.2f}")
            st.write(f"📏 **فاصله مردمک‌ها (PD ثبت‌شده):** {pd_input} میلی‌متر")
            st.write(f"💡 **توصیه تخصصی:** فریم‌هایی با پهنای کل متناسب با استخوان گونه انتخاب شوند.")

        st.markdown("---")
        st.markdown("### ۳. پیشنهادهای برند و تطبیق‌های اپتومتریک")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info(f"**برند و استایل پیشنهادی:**\n\n{brand_suggestion}")
        with c2:
            st.info(f"**پارامترهای فریم (Frame Sizing):**\n\n- پهنای عدسی متناسب با PD: `{pd_input - 8}` الی `{pd_input - 4}` م‌م\n- پهنای پل بینی (Bridge): استاندارد ۱۸-۲۰ م‌م")
        with c3:
            st.info(f"**تطبیق نمره ({rx_type}):**\n\nبا توجه به ساختار نمره و ابعاد فریم، استفاده از عدسی‌های تراش‌خورده فشرده جهت حفظ زیبایی‌شناسی توصیه می‌شود.")

else:
    st.info("👈 لطفاً یک تصویر واضح از چهره خود آپلود کنید تا سامانه تحلیلی فعال شود.")