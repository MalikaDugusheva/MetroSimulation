from collections import defaultdict, deque
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional

class Istasyon:
    """
    Metro istasyonlarını temsil eden sınıf.
    - idx: İstasyon kimliği (örneğin "M1")
    - ad: İstasyon adı (örneğin "Üsküdar")
    - hat: Metro hattı (örneğin "Marmaray")
    - komsular: Komşu istasyonlar (bağlantı süresi ile birlikte saklanır)
    """
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        """Bu fonksiyon, iki istasyon arasında belirtilen süre ile bağlantı ekler."""
        self.komsular.append((istasyon, sure))

class MetroAgi:
    """
    Metro ağını modelleyen sınıf.
    - istasyonlar: Metro istasyonlarını ID'ye göre saklar.
    - hatlar: Metro hatlarına göre istasyonları gruplar.
    - graf: Metro ağını networkx ile modellemek için kullanılır.
    """
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)
        self.graf = nx.Graph()

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        """Metro ağına yeni bir istasyon ekler."""
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)
            self.graf.add_node(ad, hat=hat)  # Görselleştirme için düğüm ekler

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        """İki istasyon arasında bağlantı oluşturur."""
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
        self.graf.add_edge(istasyon1.ad, istasyon2.ad, weight=sure)  # Graf modeline ekler
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[str]]:
        """BFS algoritması ile en az aktarmalı rotayı bulur."""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        kuyruk = deque([(baslangic, [baslangic.ad])])
        ziyaret_edildi = set()

        while kuyruk:
            mevcut, yol = kuyruk.popleft()
            if mevcut.idx == hedef.idx:
                return yol
            for komsu, _ in mevcut.komsular:
                if komsu.idx not in ziyaret_edildi:
                    kuyruk.append((komsu, yol + [komsu.ad]))
                    ziyaret_edildi.add(komsu.idx)
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[str], int]]:
        """A* algoritması ile en hızlı rotayı bulur."""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        pq = [(0, id(baslangic), baslangic, [baslangic.ad])]
        ziyaret_edildi = {}
        
        while pq:
            sure, _, mevcut, yol = heapq.heappop(pq)
            if mevcut.idx in ziyaret_edildi and ziyaret_edildi[mevcut.idx] <= sure:
                continue
            ziyaret_edildi[mevcut.idx] = sure
            if mevcut.idx == hedef.idx:
                return yol, sure
            for komsu, ek_sure in mevcut.komsular:
                heapq.heappush(pq, (sure + ek_sure, id(komsu), komsu, yol + [komsu.ad]))
        return None

    def rotayi_ciz(self, rota: List[str]):
        """Metro ağını ve belirlenen rotayı görselleştirir."""
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(self.graf)
        nx.draw(self.graf, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        if rota:
            edges = [(rota[i], rota[i+1]) for i in range(len(rota) - 1)]
            nx.draw_networkx_edges(self.graf, pos, edgelist=edges, edge_color='red', width=2)
        plt.show()

if __name__ == "__main__":
    metro = MetroAgi()
    
    metro.istasyon_ekle("M1", "Üsküdar", "Marmaray")
    metro.istasyon_ekle("M2", "Sirkeci", "Marmaray")
    metro.istasyon_ekle("M3", "Yenikapı", "Marmaray")
    metro.istasyon_ekle("M4", "Bayrampaşa", "M1B")
    metro.istasyon_ekle("M5", "Sultangazi", "M7")
    metro.istasyon_ekle("M6", "Şişli-Mecidiyeköy", "M2")
    
    metro.baglanti_ekle("M1", "M2", 4)
    metro.baglanti_ekle("M2", "M3", 2)
    metro.baglanti_ekle("M3", "M4", 6)
    metro.baglanti_ekle("M4", "M5", 8)
    metro.baglanti_ekle("M5", "M6", 10)
    metro.baglanti_ekle("M3", "M6", 5)
    
    print("\nÜsküdar'dan Sultangazi'ye en az aktarmalı rota:")
    bfs_rota = metro.en_az_aktarma_bul("M1", "M5")
    if bfs_rota:
        print(" -> ".join(bfs_rota))
        metro.rotayi_ciz(bfs_rota)
    else:
        print("Rota bulunamadı.")
    
    print("\nÜsküdar'dan Sultangazi'ye en hızlı rota:")
    astar_sonuc = metro.en_hizli_rota_bul("M1", "M5")
    if astar_sonuc:
        astar_rota, sure = astar_sonuc
        print(f"{sure} dakika: " + " -> ".join(astar_rota))
        metro.rotayi_ciz(astar_rota)
    else:
        print("Rota bulunamadı.")
        