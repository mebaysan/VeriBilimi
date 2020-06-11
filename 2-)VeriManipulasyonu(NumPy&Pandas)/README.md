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
- [Pandas](#pandas)

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
# Pandas
NumPy'ın özelliklerini kullanarak NumPy'dan daha gelişmiş işlemleri yapabilmemize olanak sağlayacaktır.