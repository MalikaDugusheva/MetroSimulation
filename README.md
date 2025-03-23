# İstanbul Metro Simülasyonu
Bu projede, İstanbul metro ağını modelleyerek Üsküdar-Sultangazi arasındaki en kısa ve en hızlı rotaları bulan bir simülasyon oluşturdum.Breadth-First Search (BFS) ve A algoritmaları* kullanarak en az aktarmalı ve en hızlı rotaları hesapladım. Ayrıca, NetworkX ve Matplotlib ile görselleştirme yaptım.

## Kullanılan Teknolojiler ve Kütüphaneler
networkx:Metro ağını modellemek için kullanılır.
matplotlib:Metro ağının görselleştirilmesi için kullanılır.
collections.deque:BFS (en az aktarmalı rota) algoritması için çift taraflı kuyruk yapısı sağlar.   
heapq:A* algoritması için öncelikli kuyruk yapısını sağlar.  
defaultdict:Metro istasyonlarını ve hatlarını saklamak için kullanılır.

### Algoritmaların Çalışma Mantığı
BFS Algoritması:Kuyruk (queue) veri yapısını kullanarak tüm komşu istasyonları katman katman ziyaret eder.Önce en kısa mesafeli yolları kontrol ederek en az aktarmalı rotayı hesaplar.
A* Algoritması:Öncelikli kuyruk (heapq) kullanarak en kısa sürede gidebileceği istasyonu önceliklendirir.Heuristic (öngörü) fonksiyonu kullanarak gereksiz yolları elemek için tahmin yapar.Bu şekilde hedefe ulaşan en hızlı rotayı bulur.

#### Neden Bu Algoritmaları Kullandık?
Bir metro simülasyonu oluşturduğumdan dolayı kullanılabilecek en mantıklı algoritmaları seçtim.BFS, en az aktarma sayısı gerektiğinde en iyi sonucu verir.A* algoritması, hedefe en hızlı ulaşımı sağlama amacımız varsa en uygun algoritmadır.NetworkX ile metro ağını modelleyerek görselleştirme yapmak için en uygun algoritmadır.

##### Örnek Kullanım ve Test Sonuçları
BFS (En Az Aktarmalı Rota) Çıktısı aşağıdaki gibidir.
Üsküdar'dan Sultangazi'ye en az aktarmalı rota:
Üsküdar -> Sirkeci -> Yenikapı -> Bayrampaşa -> Sultangazi

A* (En Hızlı Rota) Çıktısı aşağıdaki gibidir.
Üsküdar'dan Sultangazi'ye en hızlı rota:
20 dakika: Üsküdar -> Yenikapı -> Şişli-Mecidiyeköy -> Sultangazi

Grafiksel Çıktı aşağıdaki gibidir.
Metro ağı düğümler (istasyonlar) ve kenarlar (bağlantılar) ile çizilir.
Mavi noktalar: Metro istasyonlarını temsil eder.
Gri çizgiler: Metro hatlarını gösterir.
Kırmızı çizgiler: Seçilen en iyi rotayı gösterir.

###### Projeyi Geliştirme Fikirleri
Gerçek Zamanlı Trafik Verisi Kullanımı:Metro hatlarının yoğunluk bilgisine göre en hızlı rota değiştirilebilir.
Mobil ve Web Uygulaması Entegrasyonu:Bir mobil uygulama veya web platformu geliştirerek kullanıcıların metro ağında en hızlı rotayı bulmasını sağlayabiliriz.

