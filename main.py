import io
import math
import os
import html
import logging
import pandas as pd
import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION & METADATA
# ==========================================
st.set_page_config(
    page_title="Cuma Portal | Manevi Rehber",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CUSTOM CSS & SECURITY (KOPYALAMA VE SEÇİM ENGELİ)
# ==========================================
st.markdown("""
    <style>
    /* Metin Seçimini ve Kopyalamayı Tamamen Engelleme */
    body, div, p, span, h1, h2, h3, h4, h5, h6, table, ul, li {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
        -webkit-touch-callout: none !important;
    }
    
    /* Özel Tasarım Öğeleri */
    .main-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #0D9488 100%);
        padding: 2.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #0D9488;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 1.2rem;
        color: #1e293b;
    }
    
    .arabic-text {
        font-family: 'Traditional Arabic', 'Amiri', serif;
        font-size: 1.4rem;
        direction: rtl;
        text-align: right;
        color: #1E3A8A;
        line-height: 2.2;
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
    }

    .footer-text {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding: 1rem;
        border-top: 1px solid #e2e8f0;
    }
    </style>
    
    <script>
    // Sağ tık menüsünü engelle
    document.addEventListener('contextmenu', event => event.preventDefault());
    
    // Klavye kısayollarını engelle (Ctrl+C, Ctrl+V, Ctrl+U, Ctrl+S, Ctrl+A vb.)
    document.onkeydown = function(e) {
        if (e.ctrlKey && (e.keyCode === 67 || e.keyCode === 86 || e.keyCode === 85 || e.keyCode === 83 || e.keyCode === 65)) {
            return false;
        }
    };
    
    // Panoya kopyalamayı (Clipboard) engelle
    document.addEventListener('copy', (event) => {
        event.preventDefault();
        alert("Bu sitedeki içeriklerin kopyalanması Fikir ve Sanat Eserleri Kanunu gereği yasaktır.");
    });
    </script>
""", unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR NAVIGATION
# ==========================================
st.sidebar.image("https://img.icons8.com/color/96/mosque.png", width=80)
st.sidebar.title("Cuma Portalı")
st.sidebar.caption("İlmi ve Manevi Bilgi Platformu")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigasyon Menü",
    [
        "🏠 Ana Sayfa & Genel Bakış",
        "📖 Cuma Suresi (Tüm Ayetler ve Tefsiri)",
        "📜 Ayetler ve Sahih Hadisler",
        "⚖️ Cuma İbadeti, Hutbe ve Fıkhı",
        "🕌 Adım Adım Cuma Namazının Kılınışı",
        "💬 Âlimlerin ve Velîlerin Görüşleri",
        "⚖️ Hukuki Bildirim & Kullanım Şartları"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 *Bilgi:* Bu platform yalnızca bilgi ve farkındalık paylaşımı amacıyla kurulmuştur.")

# ==========================================
# 4. PAGE CONTENT MODULES
# ==========================================

# --- 1. ANA SAYFA ---
if menu == "🏠 Ana Sayfa & Genel Bakış":
    st.markdown("""
        <div class="main-header">
            <h1>🕌 CUMANIN BEREKETİ VE ANLAMI</h1>
            <p>Müslümanların Haftalık Bayramı, Birlik ve İbadet Günü</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="card">
                <h3>✨ Müminlerin Bayramı</h3>
                <p>Cuma günü, İslam aleminde haftalık toplanma, kaynaşma ve manevi yenilenme günüdür. Hadis-i şeriflerde günlerin en hayırlısı olarak nitelendirilmiştir.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="card">
                <h3>🤝 Toplumsal Dayanışma</h3>
                <p>Omuz omuza kılınan Cuma namazı, Müslümanlar arasındaki sevgiyi, vahdeti ve sosyal dayanışmayı pekiştiren en önemli ibadetlerdendir.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card">
                <h3>🤲 İcabet Saati</h3>
                <p>Cuma gününde duaların kabul olacağı hususi bir "İcabet Saati" bulunmaktadır. Bu vakti zikir ve dua ile geçirmek müstahaptır.</p>
            </div>
        """, unsafe_allow_html=True)

    st.subheader("📌 Cuma Gününün Önemli Hususiyetleri")
    st.markdown("""
    * **Hz. Âdem'in Yaratılışı:** İlk insan ve peygamber Hz. Âdem (a.s.) Cuma günü yaratılmış, o gün cennete konulmuş ve yine o gün yeryüzüne indirilmiştir (Müslim, Cuma 17).
    * **Duaların Kabulü:** Gün içinde duaların geri çevrilmediği gizli bir icabet vakti mevcuttur (Buhârî, Cuma 37).
    * **Günahlara Kefaret:** Güzelce abdest alınıp edep ile kılınan Cuma namazı, iki Cuma arasındaki küçük günahlara kefaret olur (Müslim, Cuma 27).
    """)

# --- 2. CUMA SURESİ (TÜM AYETLER VE TEFSİRİ) ---
elif menu == "📖 Cuma Suresi (Tüm Ayetler ve Tefsiri)":
    st.title("📖 Cuma Suresi ve Eksiksiz Tefsiri (11 Ayet)")
    st.caption("Kaynak: Diyanet İşleri Başkanlığı Kur'an Yolu Tefsiri & İbn Kesir Tefsiri")
    st.markdown("---")

    st.info("Cuma Suresi, Medine döneminde nazil olmuş olup toplam 11 ayettir. Adını 9. ayette geçen ve topluluk/cuma namazı anlamındaki 'El-Cumu'a' kelimesinden almıştır.")

    # Ayet 1
    st.subheader("🔹 1. Ayet")
    st.markdown("""<div class="arabic-text">يُسَبِّحُ لِلَّهِ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ الْمَلِكِ الْقُدُّوسِ الْعَزِيزِ الْحَكِيمِ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** Göklerde ve yerde ne varsa, mülkün sahibi, eksiklikten münezzeh, mutlak güç sahibi, hüküm ve hikmet sahibi olan Allah'ı tespih eder.")

    # Ayet 2
    st.subheader("🔹 2. Ayet")
    st.markdown("""<div class="arabic-text">هُوَ الَّذِي بَعَثَ فِي الْأُمِّيِّينَ رَسُولًا مِّنْهُمْ يَتْلُو عَلَيْهِمْ آيَاتِهِ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ الْكِتَابَ وَالْحِكْمَةَ وَإِن كَانُوا مِن قَبْلُ لَفِي ضَلَالٍ مُّبِينٍ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** Ümmîlere aralarından, kendilerine onun ayetlerini okuyan, onları arındıran, onlara kitabı ve hikmeti öğreten bir peygamber gönderen O'dur. Şüphesiz onlar önceden apaçık bir sapıklık içindeydiler.")

    # Ayet 3
    st.subheader("🔹 3. Ayet")
    st.markdown("""<div class="arabic-text">وَآخَرِينَ مِنْهُمْ لَمَّا يَلْحَقُوا بِهِمْ ۚ وَهُوَ الْعَزِيزُ الْحَكِيمُ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** O (peygamber), henüz kendilerine katılamamış olan diğer insanlara da gönderilmiştir. O, mutlak güç sahibidir, hüküm ve hikmet sahibidir.")

    # Ayet 4
    st.subheader("🔹 4. Ayet")
    st.markdown("""<div class="arabic-text">ذَلِكَ فَضْلُ اللَّهِ يُؤْتِيهِ مَن يَشَاءُ ۚ وَاللَّهُ ذُو الْفَضْلِ الْعَظِيمِ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** İşte bu, Allah'ın lütfudur; onu dilediğine verir. Allah büyük lütuf sahibidir.")

    # Ayet 5
    st.subheader("🔹 5. Ayet")
    st.markdown("""<div class="arabic-text">مَثَلُ الَّذِينَ حُمِّلُوا التَّوْرَاةَ ثُمَّ لَمْ يَحْمِلُوهَا كَمَثَلِ الْحِمَارِ يَحْمِلُ أَسْفَارًا ۚ بِئْسَ مَثَلُ الْقَوْمِ الَّذِينَ كَذَّبُوا بِآيَاتِ اللَّهِ ۚ وَاللَّهُ لَا يَهْدِي الْقَوْمَ الظَّالِمِينَ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** Kendilerine Tevrat yükletilip de sonra onu (gereği gibi) taşımayanların durumu, ciltlerce kitap taşıyan eşeğin durumu gibidir. Allah'ın ayetlerini yalanlayan topluluğun durumu ne kötüdür! Allah zalim toplumu hidayete erdirmez.")

    # Ayet 6
    st.subheader("🔹 6. Ayet")
    st.markdown("""<div class="arabic-text">قُلْ يَا أَيُّهَا الَّذِينَ هَادُوا إِن زَعَمْتُمْ أَنَّكُمْ أَوْلِيَاءُ لِلَّهِ مِن دُونِ النَّاسِ فَتَمَنَّوُا الْمَوْتَ إِن كُنتُمْ صَادِقِينَ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** De ki: 'Ey Yahudiler! Eğer (diğer insanları bırakıp da) yalnız sizin Allah'ın dostları olduğunuzu iddia ediyorsanız, iddianızda samimi iseniz ölümü temenni edin bakalım!'")

    # Ayet 7
    st.subheader("🔹 7. Ayet")
    st.markdown("""<div class="arabic-text">وَلَا يَتَمَنَّوْنَهُ أَبَدًا بِمَا قَدَّمَتْ أَيْدِيهِمْ ۚ وَاللَّهُ عَلِيمٌ بِالظَّالِمِينَ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** Ama önceden yaptıklarından dolayı asla ölümü temenni etmezler. Allah zalimleri çok iyi bilmektedir.")

    # Ayet 8
    st.subheader("🔹 8. Ayet")
    st.markdown("""<div class="arabic-text">قُلْ إِنَّ الْمَوْتَ الَّذِي تَفِرُّونَ مِنْهُ فَإِنَّهُ مُلَاقِيكُمْ ۖ ثُمَّ تُرَدُّونَ إِلَىٰ عَالِمِ الْغَيْبِ وَالشَّهَادَةِ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** De ki: 'Şüphe yok ki, sizin kendisinden kaçıp durduğunuz ölüm var ya, o mutlaka sizi bulacaktır. Sonra görüleni ve görülmeyeni bilen Allah'a döndürüleceksiniz de O size yaptıklarınızı haber verecektir.'")

    # Ayet 9
    st.subheader("🔹 9. Ayet (Cuma Namazına Çağrı)")
    st.markdown("""<div class="arabic-text">يَا أَيُّهَا الَّذِينَ آمَنُوا إِذَا نُودِيَ لِلصَّلَاةِ مِن يَوْمِ الْجُمُعَةِ فَاسْعَوْا إِلَىٰ ذِكْرِ اللَّهِ وَذَرُوا الْبَيْعَ ۚ ذٰلِكُمْ خَيْرٌ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** Ey iman edenler! Cuma günü namaz için çağrı yapıldığı zaman, hemen Allah'ı anmaya koşun ve alışverişi bırakın. Eğer bilirseniz, bu sizin için çok hayırlıdır.")
    
    with st.expander("📚 9. Ayetin Fıkhi Tefsiri"):
        st.markdown("""
        * **Ezanın Hükmü:** Ayette geçen çağrı (nida), Cuma namazı için okunan dış ezandır. Ezan okunduktan sonra alışveriş yapmak ve ticari faaliyetlerle meşgul olmak dinen tahrîmen mekruh/yasaktır.
        * **Caminin Yolu:** "Koşun" ifadesi bedenen koşa koşa gitmek değil, manevi bir iştiyakla, aceleyle ve öncelik vererek camiye yönelmek demektir.
        """)

    # Ayet 10
    st.subheader("🔹 10. Ayet (Namaz Sonrası Rızık Arayışı)")
    st.markdown("""<div class="arabic-text">فَإِذَا قُضِيَتِ الصَّلَاةُ فَانتَشِرُوا فِي الْأَرْضِ وَابْتَغُوا مِن فَضْلِ اللَّهِ وَاذْكُرُوا اللَّهَ كَثِيرًا لَّعَلَّكُمْ تُفْلِحُونَ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** Namaz kılındıktan sonra yeryüzüne dağılın ve Allah'ın lütfundan (rızkınızı) arayın. Allah'ı çokça anın ki kurtuluşa eresiniz.")

    # Ayet 11
    st.subheader("🔹 11. Ayet")
    st.markdown("""<div class="arabic-text">وَإِذَا رَأَوْا تِجَارَةً أَوْ لَهْوًا انفَضُّوا إِلَيْهَا وَتَرَكُوكَ قَائِمًا ۚ قُلْ مَا عِندَ اللَّهِ خَيْرٌ مِّنَ اللَّهْوِ وَمِنَ التِّجَارَةِ ۚ وَاللَّهُ خَيْرُ الرَّازِقِينَ</div>""", unsafe_allow_html=True)
    st.markdown("**Meal:** Onlar bir ticaret veya eğlence gördükleri zaman hemen oraya dağılıverdiler ve seni ayakta (hutbede) bıraktılar. De ki: 'Allah'ın katında bulunan, eğlenceden de ticaretten de hayırlıdır. Allah rızık verenlerin en hayırlısıdır.'")

# --- 3. AYETLER VE SAHİH HADİSLER ---
elif menu == "📜 Ayetler ve Sahih Hadisler":
    st.title("📜 Cuma Günü Hakkındaki Ayetler ve Sahih Hadisler")
    st.markdown("---")

    st.subheader("📌 Konuyla İlgili Diğer Ayet-i Kerimeler")
    st.markdown("""
    * **Bakara Suresi, 222:** (Temizlik ve arınma hususu, Cuma günü guslünün önemine zemin teşkil eder.)
    * **Âl-i İmran Suresi, 103:** "Allah'ın ipine hepiniz sımsıkı sarılın. Dağılıp ayrılmayın..." (Cuma namazındaki toplumsal bütünleşmeyi ifade eder.)
    """)

    st.markdown("---")
    st.subheader("📌 Genişletilmiş Sahih Hadis-i Şerif Külliyatı")

    hadisler = [
        {
            "metin": "Üzerine güneş doğan en hayırlı gün Cuma günüdür. Âdem o gün yaratıldı, o gün cennete konuldu ve o gün cennetten çıkarıldı. Kıyamet de Cuma gününden kopacaktır.",
            "kaynak": "Müslim, Cuma 17, (854); Tirmizî, Cuma 1, (488)"
        },
        {
            "metin": "Bir kimse güzelce abdest alır, sonra cumaya gelir, sessizce hutbeyi dinlerse, o cumadan gelecek cumaya kadar olan günahları ve üç gün fazlası bağışlanır.",
            "kaynak": "Müslim, Cuma 27, (857)"
        },
        {
            "metin": "Cuma gününde öyle bir saat vardır ki, Müslüman bir kul o saatte namaz kılarken Allah’tan bir şey isterse, Allah ona istediğini mutlaka verir.",
            "kaynak": "Buhârî, Cuma 37; Müslim, Cuma 13, (852)"
        },
        {
            "metin": "Cuma namazına gitmek, mazereti olmayan akıl baliğ her Müslümana farzdır.",
            "kaynak": "Ebu Davud, Salat 208, (1067)"
        },
        {
            "metin": "Kim Cuma günü mazeretsiz olarak üç defa Cuma namazını terk ederse, Allah onun kalbini mühürler (iyilikten mahrum bırakır).",
            "kaynak": "Tirmizî, Cuma 7, (491); İbn Mâce, İkame 93"
        },
        {
            "metin": "Cuma günü bana çokça salavat getirin. Çünkü sizin salavatlarınız bana arz olunur.",
            "kaynak": "Ebu Davud, Salat 207; İbn Mâce, Cenaze 65"
        },
        {
            "metin": "Cuma günü gusledenin, misvak kullananın ve gücü yettiğince güzel koku sürenin, ardından camiye gidip cemaati rahatsız etmeden namaz kılanın günahları affolunur.",
            "kaynak": "Buhârî, Cuma 6, 12"
        }
    ]

    for h in hadisler:
        st.markdown(f"""
            <div class="card">
                <p style="font-size: 1.1rem; font-style: italic;">"{h['metin']}"</p>
                <p style="text-align: right; font-weight: bold; color: #0D9488;">— {h['kaynak']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- 4. FIKIH VE İBADET ---
elif menu == "⚖️ Cuma İbadeti, Hutbe ve Fıkhı":
    st.title("⚖️ Cuma Namazının Fıkhı, Şartları, Hutbenin Önemi ve Edep Usulleri")
    st.markdown("---")

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("📋 Cuma Namazının Farz Olma Şartları (Vücub Şartları)")
        st.markdown("""
        1. **Müslüman olmak**
        2. **Erkek olmak** (Kadınlara farz değildir, kıldıkları takdirde öğle namazı yerine geçer)
        3. **Hür olmak**
        4. **Mukim olmak** (Seferî / yolcu olmamak)
        5. **Sıhhatli olmak** (Camiye gidemeyecek kadar mazeretli veya hasta olmamak)
        6. **Gözleri görmek ve yürümeye muktedir olmak**
        """)

    with col_b:
        st.subheader("✨ Cuma Gününün Sünnet ve Adapları")
        st.markdown("""
        * 🧼 **Gusül Abdesti Almak:** Cuma namazı öncesi yıkanmak müekked sünnettir.
        * 🪥 **Misvak / Diş Temizliği:** Ağız kokusunu gidermek.
        * 👔 **Temiz Elbise Giymek:** Beyaz ve temiz kıyafetler tercih etmek.
        * 🌸 **Güzel Koku Sürünmek:** Misk vb. güzel kokular kullanmak.
        * 🕌 **Erkenden Camiye Gitmek:** İlk saflarda yer almaya çalışmak.
        * 📖 **Kehf Suresi'ni Okumak:** Cuma günü Kehf Suresi'ni okuyanın iki cuma arası nurla dolacağı bildirilmiştir.
        * 🤲 **Salavat Getirmek:** Efendimiz (s.a.v.)'e bolca salatü selam okumak.
        """)

    st.markdown("---")
    st.subheader("📜 Hutbenin Önemi, Şartları ve Dinleme Âdabı")
    st.markdown("""
    Cuma namazının sıhhatinin en temel rükünlerinden biri de **Hutbe**dir. Hutbe, sadece bir hitabet kürsüsü değil, Müslümanların haftalık manevi mektebi ve toplumsal şuur merkezidir.

    * **Hutbenin Şartları ve Önemi:**
      * Hutbe, Cuma namazının farzından **önce** okunur (Önce hutbe, sonra namaz sırası esastır).
      * Hutbede Allah'a hamt, Peygamber Efendimiz'e (s.a.v.) salatü selam ve cemaate takva (Allah'tan korkma) tavsiyesi yer almalıdır. Ayrıca cemaatin anlayacağı dilde nasihatleri içermelidir.
      * Toplumun güncel manevi meselelerine ışık tutan, birliği ve kardeşliği pekiştiren ilahi bir ikaz niteliğindedir.

    * **Hutbe Dinleme Âdabı ve Yasaklar:**
      * **Mutlak Sessizlik:** Hutbe okunmaya başlandığı andan itibaren imamı dinlemek farz hükmündedir. 
      * **Konuşma Yasağı:** Hutbe okunurken yanındakine "sus" demek bile mekruhtur/yasaktır. Hadis-i şerifte buyrulduğu üzere: *"İmam hutbe irat ederken arkadaşına 'sus' dahi desen, boş söz söylemiş olursun ve Cumanın sevabı (ecri) zayi olur."* (Buhârî, Cuma 36).
      * **Meşguliyetlerin Bırakılması:** Telefonla oynamak, tespih çekmek, uyuklamak veya başka şeylerle meşgul olmak hutbenin ruhuna ve edep kurallarına aykırıdır. Tüm dikkat ve kulaklar hutbeye verilmelidir.
    """)

# --- 5. ADIM ADIM CUMA NAMAZININ KILINIŞI ---
elif menu == "🕌 Adım Adım Cuma Namazının Kılınışı":
    st.title("🕌 Cuma Namazının Detaylı Kılınış Rehberi")
    st.caption("Hanefi Mezhebine Göre Cuma Namazının Sıralaması ve Kılınışı")
    st.markdown("---")

    st.info("Cuma namazı, Cuma günü öğle namazının vaktinde kılınır. Toplamda **10 rekat** (4 rekat ilk sünnet + 2 rekat farz + 4 rekat son sünnet) olarak eda edilir. Arzusuna göre cemaat ardından Zühr-i Âhir ve Vaktin Son Sünnetini de kılar.")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1️⃣ Cuma İlk Sünneti (4 Rekat)",
        "2️⃣ İç Ezan & Hutbe",
        "3️⃣ Cuma Farzı (2 Rekat)",
        "4️⃣ Cuma Son Sünneti (4 Rekat)",
        "5️⃣ Zühr-i Âhir ve Vaktin Son Sünneti"
    ])

    with tab1:
        st.subheader("🔹 1. Cuma Namazının İlk Sünneti (4 Rekat)")
        st.markdown("""
        Öğle ezanı okunduktan sonra camiye girilip eda edilen ilk sünnettir. Aynen Öğle namazının ilk sünneti gibi kılınır.

        * **Niyet:** *"Niyet ettim Allah rızası için Cuma namazının ilk sünnetini kılmaya."*
        * **1. Rekat:** Tekbir alınır (*Allahü Akbar*), eller bağlanır. *Sübhâneke*, *Eûzü-Besmele*, *Fatiha Suresi* ve bir zammı sure (veya en az 3 kısa ayet) okunur. Rükû ve secdeler yapılır.
        * **2. Rekat:** Ayağa kalkılır, *Besmele*, *Fatiha Suresi* ve zammı sure okunur. Rükû ve secdelerden sonra oturulur (İlk Oturuş). Sadece *Ettehiyyâtü* duası okunur ve ayağa kalkılır.
        * **3. Rekat:** *Besmele*, *Fatiha Suresi* ve zammı sure okunur. Rükû ve secdeler yapılır.
        * **4. Rekat:** *Besmele*, *Fatiha Suresi* ve zammı sure okunur. Rükû ve secdelerin ardından son oturuşa geçilir.
        * **Son Oturuş:** *Ettehiyyâtü*, *Salli-Barik* ve *Rabbena* duaları okunarak sağa ve sola selam verilir.
        """)

    with tab2:
        st.subheader("🔹 2. İç Ezan ve Hutbe")
        st.markdown("""
        İlk sünnet kılındıktan sonra müezzin minberin önünde **iç ezanı** okur.

        * **Hutbe Sırası:** Hatip (İmam) minbere çıkar, oturur. İç ezan bittikten sonra ayağa kalkarak hutbeyi okur.
        * **Manevi Edep:** Cemaat bu sırada hiçbir şey konuşmaz, telefon ve tespihle ilgilenmez, tam bir huşû ile imama yönelerek hutbegi dinler.
        * Hutbe bittikten sonra müezzin kamet getirir ve farz namaz için saflar sıklaştırılır.
        """)

    with tab3:
        st.subheader("🔹 3. Cuma Namazının Farzı (2 Rekat - Cemaatle Kılınır)")
        st.markdown("""
        Cuma namazının farzı **2 rekat** olup imam liderliğinde cemaatle açıktan okunarak kılınır.

        * **Niyet:** *"Niyet ettim Allah rızası için Cuma namazının farzını kılmaya, uydum hazır olan imama."*
        * **1. Rekat:** İmamla birlikte tekbir alınır. Cemaat içinden sadece *Sübhâneke* duasını okur ve susup imamı dinler. İmam açıktan Fatiha ve zammı sure okur. Rükû ve secdeler imamla birlikte yapılır.
        * **2. Rekat:** Ayağa kalkılır. Cemaat bir şey okumaz, imamı dinler. İmam Fatiha ve zammı sure okuduktan sonra rükû ve secdeler yapılır.
        * **Son Oturuş:** *Ettehiyyâtü*, *Salli-Barik* ve *Rabbena* duaları sessizce okunur. İmamla birlikte sağa ve sola selam verilir.
        """)

    with tab4:
        st.subheader("🔹 4. Cuma Namazının Son Sünneti (4 Rekat)")
        st.markdown("""
        Farz kılındıktan ve selam verildikten sonra bireysel olarak kılınan 4 rekatlık sünnettir.

        * **Niyet:** *"Niyet ettim Allah rızası için Cuma namazının son sünnetini kılmaya."*
        * **Kılınış:** Tıpkı Cuma namazının ilk sünneti ve Öğle namazının ilk sünneti gibi 4 rekat olarak tek başına kılınır ve selam verilir.
        """)

    with tab5:
        st.subheader("🔹 5. Zühr-i Âhir ve Vaktin Son Sünneti (İhtiyat İbadetleri)")
        st.markdown("""
        Son sünnetten sonra ihtiyaten ve tedbiren eda edilen namazlardır:

        * **1. Zühr-i Âhir (4 Rekat):**
          * *"Son Öğle Namazı"* anlamına gelir. Cuma namazının şartlarında bir eksiklik olma ihtimaline binaen o günkü öğle namazı niyetine kılınır.
          * **Niyet:** *"Niyet ettim vaktine yetişip de henüz üzerimden sakıt olmayan son öğle namazının farzını kılmaya."*
          * **Kılınışı:** Öğle namazının 4 rekatlık farzı gibi kılınır (3. ve 4. rekatlarda Fatiha'dan sonra zammı sure okunmaz).
        * **2. Vaktin Son Sünneti (2 Rekat):**
          * **Niyet:** *"Niyet ettim Allah rızası için vaktin son sünnetini kılmaya."*
          * **Kılınışı:** Tıpkı Sabah namazının sünneti gibi 2 rekat kılınır ve selam verilir.
        * **Tesbihat ve Dua:** Namaz tamamlandıktan sonra Ayete'l-Kürsi okunur, 33'er defa *Sübhânallâh*, *Elhamdülillâh*, *Allâhü Akbar* denilerek dua edilir.
        """)

# --- 6. ÂLİMLERİN VE VELÎLERİN GÖRÜŞLERİ ---
elif menu == "💬 Âlimlerin ve Velîlerin Görüşleri":
    st.title("💬 İslam Âlimlerinin, Velîlerin ve Müfessirlerin Görüşleri")
    st.caption("Kaynak: Tabakat, İhyâ, Mesnevî, Risale-i Nur ve Muteber Tefsir Külliyatları")
    st.markdown("---")

    gorusler = [
        {"alim": "İmam Şâfiî (r.a.)", "soz": "Cuma günü yapılan dualar, kalbin samimiyetiyle ve ihlasla birleştiğinde kabul olunmaya en yakın vakittir. O gün ümmetin ortak zikir ve tazarru günüdür.", "kaynak": "Kitâbü'l-Ümm, c. 1"},
        {"alim": "Hasan-ı Basrî (k.s.)", "soz": "Cuma namazına yürüyerek gitmek, atılan her adımın geçmiş günahlara kefaret olmasına vesiledir. Kalbini hutbeye veren kimse o hafta manevi bir zırhla korunur.", "kaynak": "Tabakâtü'l-Kübrâ"},
        {"alim": "İmam Gazâlî (k.s.)", "soz": "Cuma günü, ahiret azığı toplamak için haftalık büyük bir pazardır. Kul, o gün kalbini dünya meşguliyetlerinden arındırıp Mevlâ'ya yönelmelidir. Hutbeyi dinlemek, kalbin pasını silen en büyük ciladır.", "kaynak": "İhyâu 'Ulûmi'd-Dîn, c. 1"},
        {"alim": "Mevlânâ Celâleddîn-i Rûmî (k.s.)", "soz": "Cuma, âşıkların buluşma günü ve visal bayramıdır. Can kulağını hutbeye ver ki, nefsani sesler sussun ve ruhun hakiki gıdasını alsın.", "kaynak": "Mesnevî-i Şerif"},
        {"alim": "Abdülkâdir-i Geylânî (k.s.)", "soz": "Cuma günü yapılan sadaka ve hayırlar, diğer günlere nazaran katbekat ecir kazandırır. Müminin bayramı olan bu günde yetimleri sevindirmek, kalplerin nurlanmasına vesiledir.", "kaynak": "Gunyetü't-Tâlibîn"},
        {"alim": "İbn Kayyim el-Cevziyye (r.a.)", "soz": "Cuma gününün diğer günlere nisbeti, Ramazan ayının diğer aylara nisbeti gibidir. Cuma günündeki icabet saati ise Kadir Gecesi gibidir.", "kaynak": "Zâdü'l-Me'âd, c. 1"},
        {"alim": "İmam-ı Rabbânî Ahmed Farukî Serhendî (k.s.)", "soz": "Cuma günü yapılan ibadetler, bütün bir haftanın ibadetlerinin özü ve ruhudur. Bugün ibadeti düzgün olanın haftası da düzgün geçer.", "kaynak": "Mektûbât-ı Rabbani, 1. Cilt"},
        {"alim": "Şah-ı Nakşibend Muhammed Bahâeddîn (k.s.)", "soz": "Cuma vakti girmeden önce kalben hazırlık yapmak, müridin edep ve samimiyetinin nişanesidir. Bedenen camide, kalben masivada olmak arzulanan meyveyi vermez.", "kaynak": "Risâle-i Bahaiyye"},
        {"alim": "Ahmet Yesevî (k.s.)", "soz": "Cuma günü cemaate devam edenlerin kalbinde hikmet pınarları kaynar. Kardeşlik bağı o saflarda pekişir.", "kaynak": "Divân-ı Hikmet"},
        {"alim": "İbn Âbidîn (r.a.)", "soz": "Cuma namazı, Müslümanların izzetini, vahdetini ve birlikteliğini temsil eden en temel şeair-i İslamiyedendir.", "kaynak": "Raddü'l-Muhtar"},
        {"alim": "Süfyan b. Uyeyne (r.a.)", "soz": "Cuma günü melekler ellerinde gümüş sahifeler ve altın kalemlerle cami kapılarında durur, erkenden gelenleri sırasıyla yazarlar.", "kaynak": "Hilyetü'l-Evliyâ"},
        {"alim": "İmam Nevevî (r.a.)", "soz": "Cuma gününde Salavat-ı Şerife'yi artırmak, Peygamber Efendimiz'e (s.a.v.) yakınlığın en kestirme yoludur.", "kaynak": "el-Ezkâr"},
        {"alim": "Molla Fenârî (r.a.)", "soz": "Hutbe, sadece bir ilat veya hitabet değil; toplumun manevi vicdanına yapılan haftalık ilahi bir ikazdır.", "kaynak": "Aynü'l-A'yân"},
        {"alim": "Ebu Talib el-Mekkî (k.s.)", "soz": "Cuma günü gusül almak ve temizlenmek, zahirdeki kirlilikten temizlendiği gibi batındaki kasveti de söküp atar.", "kaynak": "Kûtü'l-Kulûb"},
        {"alim": "Yunus Emre (k.s.)", "soz": "Cuma günü camiye varan, saf tutup Hakka duran, gönlünü Mevlaya veren, manevi felah bulur.", "kaynak": "Divan-ı Yunus Emre"},
        {"alim": "Hacı Bayram-ı Velî (k.s.)", "soz": "Omuz omuza saf tutulan Cuma vakitlerinde gıybet ve kin erir, yerini muhabbet ve ünsiyete bırakır.", "kaynak": "Makalât"},
        {"alim": "Ebu'l-Hasan el-Harakânî (k.s.)", "soz": "Cuma günü yetimin başını okşayan, bir fukaraya ekmek veren kimse, o günün bereket pınarından kanarak içer.", "kaynak": "Nûru'l-Ulûm"},
        {"alim": "İbn Kasiy el-Endelüsî (k.s.)", "soz": "Cuma günü haftanın kalbidir. Kalp diri olursa, bütün beden diri olur.", "kaynak": "Hal'u'n-Na'leyn"},
        {"alim": "Bediüzzaman Said Nursî (r.a.)", "soz": "Cuma günü, alem-i İslam'ın haftalık muazzam bir kongresidir. Müminlerin omuz omuza vermesi vahdet-i İslamiyeyi ilan eder ve hafta boyunca yapılan manevi ticaretin kâr hanesini aydınlatır.", "kaynak": "Sözler, 21. Söz / Mektûbât"},
        {"alim": "Elmalılı Hamdi Yazır (r.a.)", "soz": "Cuma namazı; hem ibadet hem toplumsal ahenk hem de müminlerin birbirinin durumundan haberdar olma vesilesidir.", "kaynak": "Hak Dini Kur'an Dili, c. 7"}
    ]

    for g in gorusler:
        st.markdown(f"""
            <div class="card">
                <h4>{g['alim']}</h4>
                <p style="font-size: 1.05rem; font-style: italic;">"{g['soz']}"</p>
                <p style="text-align: right; font-weight: bold; color: #0D9488;">— Kaynak: {g['kaynak']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- 7. HUKUKİ BİLDİRİM VE ŞARTLAR ---
elif menu == "⚖️ Hukuki Bildirim & Kullanım Şartları":
    st.title("⚖️ Hukuki Bildirim ve Kullanım Şartları")
    st.markdown("---")

    st.warning("Lütfen bu platformda yer alan içeriklerin kullanımıyla ilgili aşağıdaki hukuki hükümleri dikkatlice okuyunuz.")

    st.markdown("""
    ### 1. Amaç ve Kapsam
    Bu web sitesi, *yalnızca bilgilendirme, eğitim ve manevi farkındalık* oluşturma amacıyla kurulmuştur. Sitede yer alan dinî bilgiler, tefsir metinleri, ayet ve hadis mealleri muteber kaynaklardan derlenmiştir.

    ### 2. Ticari Kullanım Yasağı
    * Bu sitede sunulan hiçbir içerik, görsel, metin veya yazılım kodu *ticari amaçlarla kullanılamaz, satılamaz, kiralanamaz veya pazarlanamaz*.
    * Platform tamamen ücretsiz olup, herhangi bir maddi kazanç amacı gütmemektedir.

    ### 3. Fikir ve Sanat Eserleri Kanunu Koruması ve Kopyalama Yasağı
    * Bu web sitesinde yer alan tüm tasarım, derleme, metin düzenlemeleri ve kod altyapısı *5846 Sayılı Fikir ve Sanat Eserleri Kanunu* uyarınca korunmaktadır.
    * Sitede yer alan metinlerin tamamı veya bir kısmı; izin alınmaksızın *kopyalanamaz, başka sitelerde yayınlanamaz, çoğaltılamaz ve dağıtılamaz*.
    * Kod seviyesinde entegre edilen kopyalama ve sağ tık engellerinin teknik yollarla aşılması hukuki sorumluluk doğurur.

    ### 4. Sorumluluk Reddi (Disclaimer)
    * Sitede paylaşılan dini bilgiler genel bilgilendirme niteliğindedir. Fıkhi konulardaki hususi fetva ihtiyaçlarınız için Diyanet İşleri Başkanlığı Din İşleri Yüksek Kurulu'na veya yetkili mercilere başvurmanız tavsiye edilir.
    
    ---
    Son Güncelleme: 2026  
    Tüm Hakları Saklıdır.
    """)

# ==========================================
# 5. FOOTER
# ==========================================
st.markdown("""
    <div class="footer-text">
        <p>© 2026 Cuma Portalı | Bilgi Paylaşımı Amaçlıdır. Ticari Olarak Kullanılamaz ve Kopyalanamaz.</p>
    </div>
""", unsafe_allow_html=True)