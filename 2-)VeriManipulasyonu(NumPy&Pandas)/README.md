# İçindekiler
- [İçindekiler](#i̇çindekiler)
- [Veri Manipülasyonu (NumPy & Pandas)](#veri-manipülasyonu-numpy--pandas)
- [NumPy](#numpy)
  - [Nedir bu **daha verimlilik**?](#nedir-bu-daha-verimlilik)
  - [NumPy ile ndarray Oluşturmak (np.array)](#numpy-ile-ndarray-oluşturmak-nparray)
    - [Sıfır (0)  ve Birlerden (1) Oluşan ndarrayler (np.zeros & np.ones)](#sıfır-0-ve-birlerden-1-oluşan-ndarrayler-npzeros--npones)
    - [Doğrusal Dizi Oluşturmak (np.arange)](#doğrusal-dizi-oluşturmak-nparange)
    - [2 sayı arasında x adet sayı oluşturmak (np.linspace)](#2-sayı-arasında-x-adet-sayı-oluşturmak-nplinspace)
    - [Dağılımını Kendimiz Belirttiğimiz ndarray Oluşturmak (np.random.normal)](#dağılımını-kendimiz-belirttiğimiz-ndarray-oluşturmak-nprandomnormal)
    - [Rastgele Değerlerden Oluşan ndarray (np.random.randint)](#rastgele-değerlerden-oluşan-ndarray-nprandomrandint)
  - [ndarray Özellikleri](#ndarray-özellikleri)
  - [Array Yeniden Şekillendirmek (reshape)](#array-yeniden-şekillendirmek-reshape)
  - [Array Birleştirme (concatenate)](#array-birleştirme-concatenate)
  - [Array Ayırma (split)](#array-ayırma-split)
  - [Sıralama (sort)](#sıralama-sort)
  - [Array Alt Kümeleme İşlemleri (slice)](#array-alt-kümeleme-i̇şlemleri-slice)
  - [Alt Kümeler Üzerinde İşlem Yapmak (copy)](#alt-kümeler-üzerinde-i̇şlem-yapmak-copy)
  - [Fancy Index ile Elemanlara Erişmek](#fancy-index-ile-elemanlara-erişmek)
    - [Basit Index ve Fancy Index Kullanımı](#basit-index-ve-fancy-index-kullanımı)
    - [Slice ve Fancy Index Kullanımı](#slice-ve-fancy-index-kullanımı)
  - [Koşullu Eleman İşlemleri](#koşullu-eleman-i̇şlemleri)
  - [NumPy Array Üzerinde Matematiksel İşlemler](#numpy-array-üzerinde-matematiksel-i̇şlemler)
    - [ufunc Kavramı](#ufunc-kavramı)
  - [NumPy ile 2 Bilinmeyenli Denklem Çözmek](#numpy-ile-2-bilinmeyenli-denklem-çözmek)
- [Pandas](#pandas)
  - [Pandas Seri Oluşturmak](#pandas-seri-oluşturmak)
    - [Seri Oluşturmak](#seri-oluşturmak)
    - [dtype](#dtype)
    - [axes](#axes)
    - [ndim - size - values](#ndim---size---values)
    - [head(n) - tail(n)](#headn---tailn)
    - [index isimlendirme](#index-isimlendirme)
    - [index üzerinden değerlere ulaşmak](#index-üzerinden-değerlere-ulaşmak)
    - [slice](#slice)
    - [sözlük üzerinden pandas serisi oluşturmak](#sözlük-üzerinden-pandas-serisi-oluşturmak)
    - [seri birleştirmek (concat)](#seri-birleştirmek-concat)
  - [Eleman İşlemleri (Seriler)](#eleman-i̇şlemleri-seriler)
  - [Pandas DataFrame Oluşturmak](#pandas-dataframe-oluşturmak)
  - [Eleman İşlemleri (DataFrame)](#eleman-i̇şlemleri-dataframe)
    - [Sözlük (Dictionary) Üzerinden DataFrame Oluşturmak](#sözlük-dictionary-üzerinden-dataframe-oluşturmak)
    - [Index İsimlendirme](#index-i̇simlendirme)
    - [Gözlem Silmek](#gözlem-silmek)
      - [Fancy ile Gözlem Silmek](#fancy-ile-gözlem-silmek)
    - [Değişken Var mı?](#değişken-var-mı)
    - [Değişken Eklemek](#değişken-eklemek)
    - [Değişkenler Üzerinde Matematiksel İşlemler](#değişkenler-üzerinde-matematiksel-i̇şlemler)
    - [Değişken Silmek](#değişken-silmek)
  - [Gözlem ve Değişken Seçimi: loc & iloc](#gözlem-ve-değişken-seçimi-loc--iloc)

# Veri Manipülasyonu (NumPy & Pandas)
# NumPy
Numerical Python adlı Python kütüphanesidir. Python'ın bazı sayısal işlemlerde yetersiz kalmasından dolayı ihtiyaçları gidermek amacıyla ortaya çıkmış bir kütüphanedir. 
- Bilimsel hesaplamalar için kullanılır
- Arrayler / çok boyutlu arrayler ve matrisler üzerinde yüksek performanslı çalışma imkanı sunar
- 1995'te temelleri atılmıştır (matrix-sig, Guido Van Rossum) ve 2005'te hayata geçirilmiştir (Travis Oliphant).
- NumPy'a ait özel bir veri tipi vardır. ndarray (numpy.array) olarak geçmektedir. Listelere benzerdir. Farkı ise **biraz daha verimli olması** ve vektörel operasyonlardır.

## Nedir bu **daha verimlilik**?
Pure (saf) Python'da listelerde birden fazla türde eleman tutabiliyoruz (dict,list,int,str vd.) fakat bu farklı tipteki elemanları bir listede toplarken oluşturduğumuz liste, **içerisindeki her bir eleman için bir tip bilgisi** ve ek bazı bilgiler tutmaktadır. Örnek olarak aşağıdaki gibi bir liste için 3 adet tip bilgisi tutulacaktır
```
liste = [3,5,7]
```
Fakat NumPy tarafında ise kullanılacak veri tipleri arasında bir fark yoktur. Bizi **Fixed Type** kullanmaya zorlar. Yani **3 elemanlı int tipinde bir ndarray için 3 elemanın da tip bilgisi değil de direkt olarak ndarray'in tip bilgisi (bu örnek için int) tutulur**. Gerektiğinde de tutulan bu tek tip bilgisi kullanılacak. 

Vektörel operasyonlar sayesinde matematiksel işlemlerimizi daha az kod yazarak daha hızlı bir şekilde yapabileceğiz.

## NumPy ile ndarray Oluşturmak (np.array)
NumPy'ın ndarray'leri tıpkı liste veya int vb. gibi bir veri tipidir.

NumPy'da ndarray tek boyutlu ise
Vektör, 2 boyutlu ise Matris'dir. Aynı zamanda ndarray oluştururken genelde array'in eleman sayısını belirttiğimiz parametreleri sadece n  olarak verirsek n elemanlı bir vektör oluşturur. Fakat tuple içerisinde (n,y) olarak verirsek n satırlı y sütunlu Matris olarak oluşturur.<br>Vektör örnek: `np.random.randint(0,5,3)`<br>Matris örnek: `np.random.randint(0,5(3,6))`
| Boyut | Vektör | Matris |
| ----- | ------ | ------ |
| 1     | ✓      | -      |
| 2     | -      | ✓      |



Öncelikle NumPy ile işlem yaparken her zaman öncelikle `import numpy` diyerek NumPy kütüphanesini çalıştığımız dosyaya dahil etmeliyiz. Eğer ki NumPy kütüphanesi yüklü değilse `pip install numpy` diyerek kütüphaneyi bilgisayarımıza (veya sanal ortamımıza) yükleyebiliriz.

Repo boyunca bolca `np.array` vb. gibi NumPy fonksiyonlarının kullanımını göreceğiz. Bu şu şekilde olmaktadır. `import numpy as np` Bu kod parçacığı sayesinde NumPy kütüphanesine artık `np` şeklinde ulaşabilir ve kullanabiliriz.


```
import numpy as np # NumPy'ı çağırıyoruz

nd_array = np.array([1,2,3]) # bir ndarray oluşturuyoruz

print(type(nd_array)) # oluşturduğumuz nd_array değişkeninin tipini yazdırıyoruz
```

Peki elemanlarımızdan birisi ondalıklı (float) olsaydı ne olurdu?
```
nd_array = np.array([1.56,4,5,6])

print(nd_array)

>>> [1.56  4.   5.   6.  ]
```
Ne demiştik NumPy **Fixed Type** kullanmamız konusunda bizi zorlar. Bu sebeple bütün elemanları ondalıklı (float) haline getirmiştir.

Bir ndarray oluştururken `dtype` parametresini geçerek elemanları istediğimiz tipe dönüştürebiliriz. Aşağıdaki örnek için dikkat ederseniz **1.56 olan float** değerimiz **int 1** değerine dönüşmüş oldu.
```
nd_array = np.array([1.56,4,5,6],dtype="int")

print(nd_array)

>>> [1 4 5 6]
```

### Sıfır (0)  ve Birlerden (1) Oluşan ndarrayler (np.zeros & np.ones)
0'dan oluşan 10 elemanlı bir ndarray oluşturmak istersek `np.zeros` fonksiyonunu kullanmalıyız. `dtype` parametresini geçmezsek elemanları default olarak ondalıklı (float) tipinde oluşturacaktır.
```
nd_array = np.zeros(10,dtype='int')

print(nd_array)

>>> [0 0 0 0 0 0 0 0 0 0]
``` 
Aynı şekilde sadece 1'lerden oluşan ndarray oluşturabiliriz. İlk parametreyi ((3,4)) bir adet sayı verirsek verdiğimiz sayı kadar eleman oluşturacaktır. Fakat tuple olarak verirsek ( (3,4) ) tuple'ın **ilk elemanı satır** (3 satır) **ikinci elemanı sütun** (4 sütun) olacaktır. Bu kullanım şekli `np.zeros` ve birazdan göreceğimiz `np.full` için de geçerlidir.
```
nd_array = np.ones((3,4),dtype='int')

print(nd_array)

>>> [[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]
```
Sadece istediğimiz bir x sayısından oluşan ndarray oluşturmak istersek `np.full` fonksiyonunu kullanmamız gerekmektedir. Aşağıdaki örnekte 2 satır 5 sütunlu sadece 5  sayısından oluşan bir ndarray oluşturduk.
```
nd_array = np.full((2,5),5)

print(nd_array)

>>> [[5 5 5 5 5]
 [5 5 5 5 5]]
```

### Doğrusal Dizi Oluşturmak (np.arange)
Doğrusal bir dizi oluşturmak istersek `np.arange` fonksiyonunu kullanmalıyız. İlk parametre başlangıç değerimizdir, ikinci parametre bitiş değerimizdir (dahil değil), 3. parametre ise opsiyonel olarak artış değerimizdir.<br>Aşağıdaki örnekte 0'dan 15'e kadar 3'er 3'er artan bir doğrusal dizi oluşturduk.
```
nd_array = np.arange(0,15,3)

print(nd_array)

>>> [ 0  3  6  9 12]
```

### 2 sayı arasında x adet sayı oluşturmak (np.linspace)
2 sayı arasında istediğimiz x adet kadar sayı oluşturmak istersek `np.linspace` fonksiyonunu kullanmalıyız. İlk parametre başlangıç sayısı, ikinci parametre bitiş sayısı, üçüncü parametre ise kaç adet sayı oluşturmak istediğimizdir. <br> Aşağıdaki örnekte 0 ile 1 arasında 5 adet sayı oluşturduk.
```
sayilar = np.linspace(0,1,5)

print(sayilar)

>>> [0.   0.25 0.5  0.75 1.  ]
```

### Dağılımını Kendimiz Belirttiğimiz ndarray Oluşturmak (np.random.normal)
İstediğimiz dağılım özelliklerine sahip ndarray oluşturmak istersek `np.random.normal` fonksiyonunu kullanmalıyız. İlk parametre ortalama, ikinci parametre standart sapmadır ve 3. parametre ise kaç elemanlı oluşturmak istediğimizdir. <br> Aşağıdaki örnekte ortalaması 5, standart sapması 12 olan 3 satır ve 4 sütundan oluşan bir ndarray oluşturduk.
```
nd_array = np.random.normal(5,12,(3,4))

print(nd_array)

>>> [[ 10.27791205   5.46191381  -1.4755878   18.96130996]
 [  6.57390375  22.63257008  18.27698455  19.13524868]
 [ -6.04889838  11.35132997   4.25517938 -14.0720058 ]]
```

### Rastgele Değerlerden Oluşan ndarray (np.random.randint)
Eğer bizim için dağılım önemli değilse ve sadece sayı üretmek istiyorsak `np.random.randint` fonksiyonunu kullanmalıyız. İlk iki parametre hangi 2 sayı arasında sayı üretmek istediğimizdir. 3. parametre ise ndarray'in kaç elemanlı olacağıdır.
```
nd_array = np.random.randint(5,20,(3,4))

print(nd_array)

>>> [[16  7 13  9]
 [13  5  9 19]
 [18 13 13 17]]
```

## ndarray Özellikleri
Oluşturduğumuz ndarray ile ilgili özellikleri temelde 4 fonksiyon ile öğrenebiliriz
- ndim -> boyut sayısı
- shape -> boyut bilgisi
- size -> toplam eleman sayısı
- dtype -> array veri tipi
```
nd = np.random.randint(0,10,10)

print(nd)
>>> [2 9 6 3 2 1 8 7 5 3]

print(nd.ndim)
>>> 1

print(nd.shape)
>>> (10,) # bu nd değişkeni tek boyutlu olduğundan boyuttaki eleman sayısını verdi

print(nd.size)
>>> 10

print(nd.dtype)
>>> int64
```

## Array Yeniden Şekillendirmek (reshape)
Oluşturduğumuz ndarray üzerinden yeni bir  nd array oluşturmak istersek reshape fonksiyonunu kullanmamız gerekmektedir. <br>
Fonksiyonların çıktısı matris veya vektör olduğundan biz de bunları tekrar istediğimiz
şekilde boyutlandırabiliriz. Bu işleme reshape denmektedir.<br>Mesela örnek olarak aşağıda oluşturduğumuz nd adındaki ndarray'i yeniden boyutlandırarak 3x3'lük bir ndarray haline getirdik ve bunu rs değişkenine atadık:
```
nd = np.arange(1,10)

rs = nd.reshape(3,3)

print(rs)

>>> [[1 2 3]
 [4 5 6]
 [7 8 9]]
```

Bazı durumlarda bazı fonksiyonlar tek boyutlu arrayleri (vektör) kabul etmemektedir.
Bu tür durumlarda tek boyutlu arrayimizi (vektör) vektör halindeki yapısını bozmadan
matris haline getirebiliriz. Bunun için de reshape fonksiyonunu kullanabiliriz. <br> Örnek olarak aşağıda doğrusal vektörümüzü 1x9'luk bir matris haline getiriyoruz. Gördüğümüz gibi yeni oluşan `arr_degisen` arrayimiz 2 boyutlu olmuştur fakat vektör halindeki bilgileri/yapısı bozulmamıştır. 
```
arr = np.arange(1,10)
print(arr)
>>> [1 2 3 4 5 6 7 8 9]
###############################

arr_degisen = arr.reshape((1,9))
print(arr_degisen)
>>> [[1 2 3 4 5 6 7 8 9]]
print(arr_degisen.ndim)
>>> 2
```

## Array Birleştirme (concatenate)
ndarray'leri birleştirmek istersek `concatenate` fonksiyonunu kullanıyoruz. 

Vektörleri birleştirmek
```
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.array([7,8,9])
xyz = np.concatenate([x,y,z])
print(xyz)
>>> [1 2 3 4 5 6 7 8 9]
```

Matrisleri satır bazında birleştirmek
```
x = np.zeros((3,4),dtype='int')
y = np.ones((3,4),dtype='int')
xy = np.concatenate([x,y])
>>> 
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]
 [1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]
```
Eğer sütun bazında birleştirmek istersek `axis` parametresini `1` olarak vermemiz gerekmektedir. Yukarıda satır bazında birleştirmesinin sebebi de axis parametresinin default olarak 0 değerini almasıdır. `0` satır'ı, `1` sütunu temsil eder.
```
# axis = 0 veya 1 değerlerini alabilir. 0 satırları 1 sütunları temsil eder
x = np.zeros((3,4),dtype='int')
y = np.ones((3,4),dtype='int')
xy = np.concatenate([x,y],axis=1)
print(xy)
>>>
[1 2 3 4 5 6 7 8 9]
[[0 0 0 0 1 1 1 1]
 [0 0 0 0 1 1 1 1]
 [0 0 0 0 1 1 1 1]]
```

## Array Ayırma (split)
Arrayleri ayırmak (parçalamak) istersek `split` fonksiyonunu kullanmalıyız. İlk parametre 0. indexten kaçıncı indexe kadar bölünecek, 2. parametre ilk parametreden itibaren kaçıncı indexe kadar bölüneceği ifade eder.<br>
Aşağıdaki örnek x ndarray'ini önce 3. indexe **kadar** ve 3'ten 5'e kadar böler, kalanı da en son bir ndarray'de toplar.
```
x = np.array([1,2,3,99,99,3,2,1])

spl = np.split(x,[3,5])

print(spl)

>>> [array([1, 2, 3]), array([99, 99]), array([3, 2, 1])]
```
Demek ki bu örnek (np.split(x,[3,5])) bize 3 adet ndarray return ediyor. Bu return edilen değerleri sırasıyla değişkenlere atamak için aşağıdaki gibi bir kullanım yapabiliriz. Bunu Pure Python'da da kullanabiliyoruz.
```
x = np.array([1,2,3,99,99,3,2,1])

a,b,c = np.split(x,[3,5])

print(a,b,c)

>>> [1 2 3] [99 99] [3 2 1]
``` 

Matrisleri bölmek için ise şu şekilde kullanım yapabiliriz.<br> Aşağıdaki örnekte matrisi iki parçaya böldük ve **dikey** olarak ilk parçanın yanına ekledik. Bunun için `vsplit` fonksiyonunu kullandık. Aynı şekilde yukarıdaki gibi böldüğümüz matrisi `ust` ve `alt` adında 2 değişkene atadık.
```
arr = np.arange(0,16,1).reshape([4,4]) # 4x4'lük bir matrisimiz oldu. 

print(np.vsplit(arr,[2])) # ilk parametre hangi ndarray bölünecek, 2. parametre hangi elemana kadar bölünecek

>>> [array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]])]

ust,alt = np.vsplit(arr,[2])
```

Matrisleri yatay olarak bölmek istersek de `hsplit` fonksiyonunu kullanabiliriz.
```
arr = np.arange(0,16,1).reshape([4,4])

print(np.hsplit(arr,[2]))

>>> [array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])]

sag,sol = np.hsplit(arr,[2])
```

## Sıralama (sort)
Tek boyutlu bir arrayi (vektör) sıralamak istersek `sort` fonksiyonunu kullanabiliriz.
```
arr = np.array([3,1,2,6,74,6,8,9,12])

print(np.sort(arr))

>>> [ 1  2  3  6  6  8  9 12 74]
```

Matrisleri sıralamak için ise yine `sort` fonksiyonunu kullanıyoruz. Fakat bu sefer `axis` parametresi ile beraber kullanıyoruz. Bİldiğimiz gibi `axis = 0` satırları ifade ederken `axis = 1` sütunları ifade etmektedir.
```
arr = np.random.normal(20,5,(3,3))

print(np.sort(arr,axis=0))
```

## Array Alt Kümeleme İşlemleri (slice)
Vektörlerde slice işlemi yapmak istersek temel komut dizilimi şu şekildedir: `array[x:y:z]` <br> Slice işlemlerinde x-y-z opsiyoneldir.
- x = kaçıncı indexten başlayacağı
- y = kaçıncı indexe kadar alacağı
- z = kaçar kaçar gideceği
```
# Vektör

arr = np.random.randint(0,10,10)

print(arr[0:3]) # 0. index ile 3. index arasını al

print(arr[:3]) # 0. index ile 3. index arasını al

print(arr[3:]) # 3. indexten sonrasını al

print(arr[1::2]) # 1. indexten son indexe kadar git 2'er 2'er atla

print(arr[-1]) # son indexi verir
```
Matrisler (çok boyutlu arrayler) üzerinde slice işlemleri yapmak için temel dizilim şu şekildedir: `arr[x:y,z:m]` <br> `y` ve `m` opsiyoneldir.
- x = satırlar kaçıncı indexten başlasın
- y = satırlar kaçıncı indexe kadar alınsın
- z = sütunlar kaçıncı indexten başlasın
- m = sütunlar kaçıncı indexe kadar alınsın
```
nd = np.random.randint(0,10,(5,5))

print(nd[:,0]) # bütün satırları seç ve sadece 0. sütunları al

print(nd[0,:]) # 0. satır ve tüm sütunlar

print(nd[0:2,0:3]) # 0 ile 2'e kadar satırlar, 0 ile 3 arası sütunlar

print(nd[0:,0:2]) # bütün satırlar, 0 ile 2. sütunlar arası
```
## Alt Kümeler Üzerinde İşlem Yapmak (copy)
Bazı durumlarda alt kümelerimiz üzerinde işlem yapmak isteriz. Bu durumlarda direk ana kümemizden seçtiğimiz alt küme üzerinde değişiklik yaparsak yaptığımız değişiklik ana kümemize de uygulanmış olur <br>
Aşağıdaki örnek kodda `alt_nd` alt kümesinin 0,0 ve 1,1 değerlerini değiştirdik. Fakat bu asıl kümemiz olan `nd` ana kümesinin de 0,0 ve 1,1 değerlerinin değişmesine sebep oldu.
```
nd = np.random.randint(0,10,(5,5))

alt_nd = nd[0:3,0:2]

alt_nd[0,0] = 1234  

alt_nd[1,1] = 56789

print(nd)
>>> [[ 1234     8     8     4     8]
 [    3 56789     4     4     4]
 [    3     4     6     2     7]
 [    7     4     8     7     9]
 [    4     9     9     3     4]]
```

Eğer yukarıdaki gibi bir sonuçla (belki problem) karşılaşmak istemiyorsak `copy` fonksiyonunu kullanmalıyız. Bu sayede alt_kume değişkenimize ana kümemizden aldığımız alt kümenin bir **kopyası** aktarılacak ve bu sayede yaptığımız değişiklikler ana kümemizde uygulanmamış olacak. Yani denemelerimiz için ana kümemizi bozmamış olacağız. <br>
Aşağıdaki örnek kodda `nd` değişkenimizin 0:3 ve 0:2 matrisinin **kopyasından** bir `alt_kume` alt kümesi oluşturuyoruz ve bunu değişkene atıyoruz. Sonrasında yaptığımız değişiklikler asıl kümemiz olan `nd` ana kümesinde uygulanmayacaktır.
```
nd = np.random.randint(0,10,(5,5))

alt_kume = nd[0:3,0:2].copy()

alt_kume[0,0] = 9999

print(nd)

>>> [[1 0 8 5 1]
 [8 0 2 2 2]
 [9 0 8 7 4]
 [4 0 2 8 0]
 [3 7 0 1 1]]
```

## Fancy Index ile Elemanlara Erişmek
Fancy kelime anlamı olarak fantastik anlamına gelmektedir. NumPy Array'lerinde ve Pandas DataFrame'lerinde daha rahat eleman seçmemize olanak sağlar.

Örnek olarak tek boyutlu bir arrayimiz var (vektör) ve bundan 1. 3. ve 5. indexteki değerleri çekmek istiyoruz. Burada yaptığımız işleme `fancy index` denmektedir.
```
nd = np.arange(0,30,3) 

istenilen_indexler = [1,3,5]

print(nd[istenilen_indexler])
```

Bu işlemi matrisler üzerinde gerçekleştirmek istersek ise erişmek istediğimiz satır ve sütunları kullanarak gerçekleştirebiliriz.
```
nd = np.arange(0,9).reshape((3,3)) # tek boyutlu arrayi, boyutlu array haline getirdik

istenilen_satir = np.array([0,1])

istenilen_sutun = np.array([1,2])

print(nd[istenilen_satir,istenilen_sutun])

>>> [1 5]
```
### Basit Index ve Fancy Index Kullanımı
Fancy Index'ler sayesinde çok rahat bir şekilde elemanlara erişebildiğimizi söylemiştik. <br> Aşağıdaki örnekte basit index ile fancy index birarada kullanılmıştır. Basit index ile 0. satır alınmış ve fancy index ile 1 ile 2. sütunlar alınmıştır.
```
nd = np.arange(0,9).reshape((3,3))

print(nd[0,[1,2]]) 

>>> [1 2]
```
### Slice ve Fancy Index Kullanımı
Aşağıdaki örnekte slice işlemi ve fancy index bir arada kullanılmıştır. 1. satırdan sonraki satırlar slice ile 1. ve 2. satırlar fancy index ile alınmıştır.
```
nd = np.arange(0,9).reshape((3,3))

print(nd[1:,[1,2]])

>>> [[4 5]
 [7 8]]
```

## Koşullu Eleman İşlemleri
Bir array içerisindeki elemanların belirli bir koşula uyup uymadığını öğrenebiliriz. <br> Aşağıdaki örnekte nd array'i içerisindeki her bir elemanın `< 4` koşuluna uyup uymadığı sorgulanmıştır.
```
nd = np.arange(0,10)

print( nd < 4)

>>> [ True  True  True  True False False False False False False]
``` 
Peki bunları tekrar bir değişkene atamak istersek ne yapacağız?
```
nd = np.arange(0,10)

dortten_kucukler = nd[nd < 4]

print(dortten_kucukler)

>>> [0 1 2 3]
```
Örneklerde kullanılan `<` işaretini Python'da bildiğimiz her karşılaştırma operatörü için kullanabiliriz
- `<` - Küçükse
- `>` - Büyükse
- `<=` - Küçük veya eşitse
- `>=` - Büyük veya eşitse
- `==` - Eşitse
- `!=` - Eşit değilse

## NumPy Array Üzerinde Matematiksel İşlemler
Bir arrayimiz var ve bütün elemanlarının 2 ile çarpılmasını istiyoruz. Bu durumda ne yapacağız?<br>
Aşağıdaki örnekte `nd` arrayinin tüm elemanları 2 ile çarpılmıştır. Tabii bunu diğer matematiksel operatörler ile de kullanmak mümkündür ( /, * vd.)
```
nd = np.arange(0,10)

print(nd*2)

>>> [ 0  2  4  6  8 10 12 14 16 18]
```
Aşağıdaki örnekte tüm elemanlardan `1` çıkarılmıştır
```
nd = np.arange(0,10)

print(nd - 1)

>>> [-1  0  1  2  3  4  5  6  7  8]
```
### ufunc Kavramı
Aslında bir üst başlıktaki matematiksel işlem örneklerini yaptığımızda da numpy arrayleri içerisinde otomatik olarak ufunc fonksiyonları çalışmaktadır. Örnek olarak `nd - 1` kodunu çalıştırdığımızda arkada bir adet `ufunc` çalışmaktadır.
```
nd = np.arange(0,10)

print(np.subtract(nd,1))

>>> [-1  0  1  2  3  4  5  6  7  8]
```
Bazı ufunc'lar:
- `np.subtract(nd,1)` -> nd arrayindeki her bir elemandan 1 çıkarır
- `np.add(nd,1)` -> nd arrayindeki her bir elemana 1 ekler
- `np.multiply(nd,2)` -> nd arrayindeki her bir elemanı 2 ile çarpar
- `np.divide(nd,2)` -> nd arrayindeki her bir elemanı 2 ile böler
- `np.power(nd,2)` -> nd arrayindeki her bir elemanın 2 üssünü alır
- `np.mod(nd,2)` -> nd arrayindeki her bir elemanın 2'e bölümünden kalanları verir
- `np.absolute(nd)` -> nd arrayindeki her bir elemanın mutlak değerini verir
- `np.log(nd)` -> nd arrayindeki her bir elemanın logaritmasını alır

## NumPy ile 2 Bilinmeyenli Denklem Çözmek
NumPy içerisindeki alt paket olan `linalg` ile lineer cebir işlemlerini gerçekleştirebiliriz.<br>
Denklemimiz şu şekildedir:
```
5 * x0 + x1 = 12

x0 + 3 * x1 = 10
```
Öncelike `a` değişkenine denklemdeki bilinmeyenlerin katsayılarını tanımlıyoruz. `5 tane x0 + 1 tane x1` ve `1 tane x0 ve 3 tane x1` anlamına gelmektedir.
```
a = np.array([[5,1],[1,3]])
```
Daha sonra `b` değişkenine katsayılara karşılık oluşmuş olan eşitliğin diğer tarafındaki ifadeleri tanımlıyoruz.
```
b = np.array([12,10])
```
Ve `cevap` değişkenimize NumPy'ın alt pakedi olan `linalg` paketinin `solve` fonksiyonu ile çözdüğümüz cevabı atıyoruz. 1. argüman ve 2. argüman arasındaki ilişki sonucunda oluşacak olan katsayıları hesapla dedik ve x1 ile x2 değerlerini bulmuş olduk.
```
cevap = np.linalg.solve(a,b)

print(cevap)

>>> [1.85714286 2.71428571]
```
Kodun son hali:
```
import numpy as np

a = np.array([[5,1],[1,3]])

b = np.array([12,10])

cevap = np.linalg.solve(a,b)

print(cevap)

>>> [1.85714286 2.71428571]
```
# Pandas
NumPy'ın özelliklerini kullanarak NumPy'dan daha gelişmiş işlemleri yapabilmemize olanak sağlayacaktır.<br>
 - Panel Data'nın kısaltılmışı olarak ortaya çıkmıştır.
 - Veri manipülasyonu ve veri analizi için yazılmıştır.
 - Açık kaynak kodludur.
 - NumPy'a alternatif değildir. Onun özelliklerini kullanan ve bunları genişleten bir kütüphanedir.
 - Pandas'ın kendisine ait veri tipi vardır. Pandas DataFrame olarak geçmektedir.
 - Pandas DataFrame'lerini NumPy arraylerinden bildiğimiz tek boyutlu arrayler (vektör) olarak düşünebiliriz
 - NumPy'daki **Fixed Type zorunluluğu Pandas'ta yoktur.** Bu sayede bir çok farklı veri tipini okuma ve yazma imkanı sağlar.
 - Ekonometrik ve finansal çalışmalar için doğmuştur.
 - Temeli 2008 yılında atılmıştır.
 - R DataFrame yapısını Python dünyasına taşımış ve DataFrame'ler üzerinde hızlı ve etkili çalışabilme imkanı sağlamıştır.

## Pandas Seri Oluşturmak
Pandas ile işlem çalışırken her zaman önce 
`import pandas` diyerek Pandas kütüphanesini çalıştığımız 
dosyaya dahil etmeliyiz. Eğer ki Pandas kütüphanesi yüklü
değilse `pip install pandas` diyerek kütüphaneyi 
bilgisayarımıza (veya sanal ortamımıza) yükleyebiliriz.


`import pandas as pd` -> Bu kod parçacığı 
sayesinde Pandas kütüphanesine artık `pd` şeklinde 
ulaşabilir ve kullanabiliriz.

Pandas Serilerinin kendine özel bir yapısı vardır. Veri yapısının yanında bir de index numaralarını tutmaktadır.
### Seri Oluşturmak
Bir Pandas serisi oluşturmak için `pd.Series` fonksiyonu kullanılır.
```
import pandas as pd

df = pd.Series([11,22,33,44,55,66,77,88,99])

print(df)
>>> 0    11
1    22
2    33
3    44
4    55
5    66
6    77
7    88
8    99
```
### dtype
Pandas serilerinin sakladığı verilerin tipini öğrenmek için ise `dtype` fonksiyonunu kullanabiliriz
```
df = pd.Series([11,22,33,44,55,66,77,88,99])

print(df.dtype)

>>> int64
```
### axes
Pandas serilerinin index bilgilerine erişebiliriz<br>
Aşağıdaki örnek için çıktımız bize indexlerin 0'dan 9'a KADAR 1'er 1'er gittiğini söylemektedir.
```
df = pd.Series([11,22,33,44,55,66,77,88,99])

print(df.axes)

>>> [RangeIndex(start=0, stop=9, step=1)]
```
### ndim - size - values
Pandas Serisinin eleman sayısını öğrenmek istersek `size` ve boyut sayısını öğrenmek istersek `ndim` fieldlarını kullanmamız gerekmektedir. Aynı zamanda serilerin `values` fieldını kullanarak sadece değerlerine erişebiliriz (index numaraları hariç). 
```
df = pd.Series([11,22,33,44,55,66,77,88,99])

print(df.size)
>>> 9

print(df.ndim)
>>> 1

print(df.values)
>>> [11 22 33 44 55 66 77 88 99]
```
### head(n) - tail(n)
Serilerin baştan `n` kadar (`head(n)`) ve sondan `n` kadar (`tail(n)`) değerlerini görüntüleyebiliriz.<br> Aşağıdaki örneklerde baştan ve sondan 5'er (n) veri görüntülenmiştir.
```
df = pd.Series([11,22,33,44,55,66,77,88,99])

print(df.head(5)) # serinin ilk 5 değerini getirir
>>> 0    11
1    22
2    33
3    44
4    55
dtype: int64

print(df.tail(5)) # serinin son 5 elemanını getirir
>>> 4    55
5    66
6    77
7    88
8    99
dtype: int64
```

### index isimlendirme
İstersek oluşturduğumuz serilerin index'lerini isimlendirebiliriz.
```
df = pd.Series([12,23,34,45,56],index=['x','y','z','w','q'])

print(df)

>>> x    12
y    23
z    34
w    45
q    56
dtype: int64
```
### index üzerinden değerlere ulaşmak
Pure Python'daki sözlük yapısında olduğu gibi Pandas Serilerinde de index'ler üzerinden karşılık geldiği değerlere erişebiliriz. <br>
Aşağıdaki örnekte bir Pandas Serisi oluşturulmuş ve index'leri isimlendirilmiştir. Ardından `x` indexindeki elemana erişilmiştir.
```
df = pd.Series([12,23,34,45,56],index=['x','y','z','w','q']) 

print(df['x'])

>>> 12
```

### slice
NumPy'da olduğu gibi Pandas'ta da slice işlemlerini gerçekleştirebiliriz. <br>
Aşağıdaki örnekte `x` indexinden `z` indexine kadar slice işlemi gerçekleştirilmiştir.
```
df = pd.Series([12,23,34,45,56],index=['x','y','z','w','q'])

print(df['x':'z']) # x index'inden z index'ine kadar slice

>>> x    12
y    23
z    34
dtype: int64
```

### sözlük üzerinden pandas serisi oluşturmak
Sadece listeler üzerinden değil sçzlük veri tipi üzerinden de pandas serileri oluşturulabilir. Sözlüğün `key` değerleri oluşan pandas serisinin indexlenmesinde kullanılır.
```
df = pd.Series({'reg':10,'log':11,'cat':12})

print(df)

>>> reg    10
log    11
cat    12
dtype: int64
```

### seri birleştirmek (concat)
Serileri birleştirerek yeni seriler üretebiliriz. Bunun için `concat` fonksiyonu kullanılmaktadır. Önemli nokta şudur ki gönderilen her parametrenin veri tipi pandas serisi olmalıdır.
```
seri1 = pd.Series([1,2,3],index=['x1','y1','z1'])

seri2 = pd.Series([4,5,6],index=['x2','y2','z2'])

df = pd.concat([seri1,seri2])

print(df)

>>> x1    1
y1    2
z1    3
x2    4
y2    5
z2    6
dtype: int64
```

## Eleman İşlemleri (Seriler)
Oluşturduğumuz pandas serileri üzerinde işlemler gerçekleştirebilmekteyiz. 
- `index` ile serinin index bilgilerine erişebilmekteyiz
- `keys` ile serinin key değerlerine ulaşabiliriz
- `list(seri.items())`  ile seriyi key-value olarak **tuple** olacak şekilde bir listeye atar
- `values` ile sadece serinin değerlerini alabiliriz
- `'x' in seri` kullanımı ile 'x' değerinin seride olup olmadığını kontrol edebiliriz
- `seri[[1,4]]` (fancy index) ile index'i 1 ve 4 olan değerleri alırız
- `seri[1:4]` ile 1 ile 4. index arasındaki değerleri alırız

```
import pandas as pd
import numpy as np

nd = np.array([1,2,34,45,677,75])
seri = pd.Series(nd)

print(seri.index) # index bilgilerine ulaşıyoruz

print(seri.keys) # key değerlerine ulaşırız

print(list(seri.items())) # key-value şeklinde tuple olarak bir listeye alırız

print(seri.values) # serinin sadece değerlerine erişiriz

# elemanları sorgulamak

print("x" in seri) # "x" değeri seri'nin içinde mi sorusunu sorduk

# fancy ile eleman seçmek

print(seri[[1,4]]) # index'i 1 ile 4 olan verileri getirdik

print(seri[1:4]) # index'i 1'den 4'e kadar olan verileri getir

```

## Pandas DataFrame Oluşturmak
Pandas DataFrame, yapısal bir veri tipidir. Excel veri yapısına benzerdir. **Pandas DataFrame Fixed Type değildir.** 

`DataFrame` fonksiyonu ile Pandas DataFrame oluşturulabilmektedir. İstersek `columns` argümanını da set ederek **değişken** isimlerini belirleyebiliriz.
```
df = pd.DataFrame([1,2,45,67,879,90],columns=["degisken_adi"])

print(df)

>>>    degisken_adi
0             1
1             2
2            45
3            67
4           879
5            90
```

Aşağıdaki örnekte NumPy arrayi oluşturulmuş ve yeniden boyutlandırılmıştır (3x3). Oluşturulan bu ndarray üzerinden bir adet Pandas DataFrame'i oluşturulmuş ve değişken (kolon) isimleri set edilmiştir. Ekrana çıktı alındıktan sonra sırasıyla değişken (kolon) isimleri tekrar değiştirilmiş ve ekrana yazılmıştır.
```
nd = np.arange(1,10).reshape((3,3))

df = pd.DataFrame(nd,columns=['var1','var2','var3'])

print(df)
>>>    var1  var2  var3
0     1     2     3
1     4     5     6
2     7     8     9

df.columns = ('deg1','deg2','deg3') # değişken isimleri değiştirildi

print(df)
>>>    deg1  deg2  deg3
0     1     2     3
1     4     5     6
2     7     8     9
```

Oluşturduğumuz Pandas DataFrame'lerine dair bilgilere aşağıdaki gibi erişebiliriz.
```
nd = np.arange(1,10).reshape((3,3))

df = pd.DataFrame(nd,columns=['var1','var2','var3'])

print(df.axes) # satır ve sütun bilgilerini verir

print(df.ndim) # boyut sayısını verir

print(df.shape) # kaça kaçlık

print(df.size) # kaç elemanlı

print(df.values) # sadece değerleri verir ve ndarray nesnesine çevirir

print(df.head(2)) # baştan 2 veri

print(df.tail(2)) # sondan 2 veri
```

## Eleman İşlemleri (DataFrame)

### Sözlük (Dictionary) Üzerinden DataFrame Oluşturmak
Bu başlık boyunca yaptığımız örnekler aşağıdaki 
DataFrame üzerinden gerçekleştirilecektir.
```
import pandas as pd
import numpy as np


s1  = np.random.randint(0,10,5)
s2  = np.random.randint(0,10,5)
s3  = np.random.randint(0,10,5)

sozluk = {'var1':s1,'var2':s2,'var3':s3}

df = pd.DataFrame(sozluk)
```

### Index İsimlendirme
Aşağıdaki örnekte, yukarıdaki başlıkta oluşturduğumuz df DataFrame'inin indexlerini yeniden isimlendiriyoruz. 5 adet argüman yollamamızın sebebi 5 adet gözlem değerine sahip olmamızdan kaynaklanmaktadır.
```
df.index = ['a','b','c','d','e']

print(df)

>>>    var1  var2  var3
a     7     3     2
b     8     6     0
c     8     1     3
d     4     6     5
e     6     8     8
```

### Gözlem Silmek
Aşağıdaki örnekte `a` gözlemi (a indexi) silinmiştir. `axis=0` kullanımı [yukarıdaki örneklerden](#array-birleştirme-concatenate) de bildiğimiz gibi satırları, `axis=1` ise sütunları ifade etmekteydi. `inplace` argümanının `True` olarak set edilmesi ise yapılan değişikliğin kalıcı olmasını sağlamaktadır. 
```
print(df)

>>>    var1  var2  var3
a     7     3     2
b     8     6     0
c     8     1     3
d     4     6     5
e     6     8     8

df.drop('a',axis=0,inplace=True)

print(df)

>>>    var1  var2  var3
b     8     6     0
c     8     1     3
d     4     6     5
e     6     8     8
```

#### Fancy ile Gözlem Silmek
Aşağıdaki örnekte yalnızca `b` ve `d` gözlemleri gelmiştir. Bunun sebebi fancy ile `c` ve `e` gözlemlerini bizim silmemizdir. Fakat `a` gözleminin gelmemesinin sebebi ise bu işlemi bir üst başlıkta `inplace=True` argümanıyla birlikte `a` gözlemini sildiğimiz aynı `df` DataFrame'i ile gerçekleştiriyor olmamızdır. Aşağıdaki örneklerde göreceğimiz üzere `c` ve `e` işlemlerine erişebileceğiz çünkü `inplace` argümanını göndermedik.
```
silinecekler = ['c','e']

print(df.drop(silinecekler,axis=0))

>>>    var1  var2  var3
b     8     6     0
d     4     6     5
```

### Değişken Var mı?
Aşağıdaki örnekte `var1` değişkeninin `df` DataFrame'i içerisinde olup olmadığı sorgulanmıştır.
```
print('var1' in df)

>>> True
```

### Değişken Eklemek
Aşağıdaki örnekte `var4` adında bir değişken eklenmiştir. Bu yapı Pure Python'dan bildiğimiz `dictionary` veri tipine benzemektedir. `var4` değişkeni olsaydı aslında onun değerini set etmiş olacaktık fakat olmadığı için mevcut DataFrame'imize `var4` adında bir değişken eklemiş olduk.
```
df['var4'] = [1,2,3,4] 

print(df)

>>>    var1  var2  var3  var4
b     8     6     0     1
c     8     1     3     2
d     4     6     5     3
e     6     8     8     4
```

### Değişkenler Üzerinde Matematiksel İşlemler
Aşağıdaki örnekte `var1` değişkeni ile `var2` değişkeninin bölümünden elde edilen sonuçlar `var4` değişkenine yazılmıştır.
```
df['var4'] = df['var1'] / df['var2'] 

print(df)

>>>    var1  var2  var3      var4
b     8     6     0  1.333333
c     8     1     3  8.000000
d     4     6     5  0.666667
e     6     8     8  0.750000
``` 

### Değişken Silmek
Aşağıdaki örnekte `var4` değişkeni silinmiştir. `axis=1` argümanının verilmesi ise silinmek istenen değerin **sütun** bazında olmasıdır. Tekrar hatırlayalım; `axis=0` satırları, `axis=1` sütunları temsil etmektedir.
```
df.drop('var4',axis=1,inplace=True) 

print(df)

>>>    var1  var2  var3
b     8     6     0
c     8     1     3
d     4     6     5
e     6     8     8
```


## Gözlem ve Değişken Seçimi: loc & iloc
Gözlem ve değişken seçimi için kullanacağımız 2 türlü yapı vardır. `loc` ve `iloc` yapıları. Değişken seçimi için zorunlu kurallarımız varsa `loc` yapısını kullanmalıyız. Fakat zorunlu kurallarımız yoksa `iloc` yapısını kullanabiliriz.<br>
Öncelikle bu bölüm için üzerinde işlem yapacağımız DataFrame'i tanımlıyoruz.
```
import pandas as pd
import numpy as np

nd = np.random.randint(1,30,(10,3))
df = pd.DataFrame(nd,columns=['var1','var2','var3'])

print(df)
>>>    var1  var2  var3
0     2    20     4
1     6    17    24
2     7     2     3
3     7    25    14
4    10     4    20
5    16    19     3
6     1    22     3
7     9    10    17
8    13    25     1
9    26    17    19
```

`loc` yapısına bir örnek gösterelim. Bu örnekte 0. index ile 3. index ve arasındakiler seçilmiştir. 3. index **DAHİLDİR**.
```
print(df.loc[0:3])
>>>    var1  var2  var3
0     2    20     4
1     6    17    24
2     7     2     3
3     7    25    14
```

`iloc` yapısının kullanıldığı bu örnek ise alışık olduğumuz indexleme mantığını kullanır. Aşağıdaki örnekte 0. indexten 3. indexe **KADAR** gözlemler seçilmiştir.
```
print(df.iloc[0:3])
>>>    var1  var2  var3
0     2    20     4
1     6    17    24
2     7     2     3
```

Bu örnekte ise en baştan 3. indexe kadar (satır - gözlem) ve en baştan 2. sütuna kadar (değişken) olan veriler seçilmiştir.
```
print(df.iloc[:3,:2])
>>>    var1  var2
0     2    20
1     6    17
2     7     2
```

Eğer değişken ve gözlemlerle ilgili **kesin** bir işaretleme (seçim) yapacaksak `loc` kullanmalıyız. Aşağıdaki örnekte 0. satır ile 3. satır arasındakiler (3. satır dahil) ve yalnızca 'var3' sütunundakiler (değişken) seçilmiştir.
```
print(df.loc[0:3,'var3'])
>>> 0     4
1    24
2     3
3    14
Name: var3, dtype: int64
```
Yukarıdaki yaptığımız işlemin aynısını `iloc` ile yapmak istersek hata alacağız. Bunun sebebi ise bizim 'var3' olarak spesifik (zorunlu) bir değişkeni seçmek istiyor olmamız. Fakat ne demiştik? Değişken ve gözlem seçmek için zorunlu kurallarımız varsa `loc` yapısını kullanmalıyız.
```
print(df.iloc[0:3,'var3'])
>>> ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types
```

Aşağıdaki örnekte `iloc` yapısı ile 0. satırdan 3. satıra **KADAR** gözlemler ve yalnıza 'var3' değişkeni seçilmiştir.
```
print(df.iloc[0:3]['var3'])
>>> 0     4
1    24
2     3
Name: var3, dtype: int64
```


