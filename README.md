# Project2-1_Enigma_machine

## 題目:破解Enigma
### 經過Enigma加密後的密文:
ZATVAWORBRQGRJSXZVNORWZBLORMEGRASLQLAFWXZYODVVTDHCIRDMNWOPNIXVKASIIIALOOSZXAMSYCQHYGPRLMSACGAWPCPAVZTMUUZCTJDVBUZAGFWMIVEZGBTLFIQDPPRZHDNK
### 提示:
最後10個字母為HEILHETLER加密後的文字。
### 目標:
找出明文

## Enigma 基礎
- 接線板，將兩字母相連，可自行設定。ex:A、R，當輸入A時，經過接線板後會變成R。

![](https://github.com/cislab-yzu/Project2-1_Enigma_machine/blob/master/Pictures/plugboard.jpg)
![](https://github.com/cislab-yzu/Project2-1_Enigma_machine/blob/master/Pictures/inputA.jpg)
- 轉盤，可自行設定轉盤起始位置，轉盤指針位置為固定，轉盤內字母的對應也是固定(非兩字母互相關聯)。
![](https://github.com/cislab-yzu/Project2-1_Enigma_machine/blob/master/Pictures/rotor.jpg)
- 反射盤，不可自行設定，也是兩字母相連的關係。
![](https://github.com/cislab-yzu/Project2-1_Enigma_machine/blob/master/Pictures/reflector.jpg)
- 轉盤動的規則:每輸入一個字母，轉盤I動一格。當轉盤I的起始位置=指針位置時，轉盤II動一格。當轉盤II的起始位置在指針位置前一格時，轉盤II、轉盤III動一格。

- 舉例:
![](https://github.com/cislab-yzu/Project2-1_Enigma_machine/blob/master/Pictures/run.jpg)
當我輸入A時，會先經過接線板轉換成R，計算A到R的距離(17)。

進入轉盤I，轉盤I起始位置確定後，從起始位置(Y)數17格(P)，對應到該轉盤的連接字母E，計算Y到E的距離(6)。

進入轉盤II，轉盤II起始位置確定後，從起始位置(D)數6格(J)，對應到該轉盤的連接字母B，計算D到B的距離(24)。

進入轉盤III，轉盤III起始位置確定後，從起始位置(H)數24格(F)，對應到該轉盤的連接字母G，計算H到G的距離(25)。

進入反射盤，從起始位置(A)數25格(Z)，對應到反射盤的連接字母T，計算A到T的距離(19)。

進入轉盤III，轉盤III起始位置確定後，從起始位置(H)數19格(A)，找出該轉盤U是對應到A，計算H到U的距離(13)。

進入轉盤II，轉盤II起始位置確定後，從起始位置(D)數13格(Q)，找出該轉盤Q是對應到Q，計算D到Q的距離(13)。

進入轉盤I，轉盤I起始位置確定後，從起始位置(Y)數13格(L)，找出該轉盤F是對應到L，計算Y到F的距離(7)。

進入接線板，從起始位置(A)數7格(H)，對應到接線板的連接字母H，輸出H。

以此繼續做下去。


## 解法
直接從最後10個輸出下手，找出能讓輸入為HEILHITLER時，輸出為IPQHUGCXZM的所有轉盤配置、接線板配置的組合。

一開始是先從接線板開始配對

一條接線:(A跟B接)，(A跟C接)，...

兩條接線:(A跟B接、C跟D接)，(A跟B接、C跟E接)...

但是發現我花了很多時間在照順序換接線方式，卻都還沒換到HEILHITLER、IPQHUGCXZM中會用到的字母，浪費了很多時間。

所以我直接換HEILHITLER、IPQHUGCXZM會用到的字母的接線，並存起來，只要有矛盾就換下一組，最後所有轉盤配置、接線方式終能找到輸入為HEILHITLER時，輸出為IPQHUGCXZM的組合就只有不到500種，時間也節省了非常多。

最後再逆推回到148 - 10之後的起始位置，並輸入密文全部之後就是解了，但也沒有找到像是句子的解，所以算是失敗了。

## 結果
雖找出了所有接線板、轉盤、轉盤起始位置、輸入，經過Enigma加密後為題目密文的字串，但卻沒有找出正確答案，猜測可能有在中途切換過轉盤之起始位置。

## 工作分配
###  1051524莊子毅 編寫基本enigma功能 各種plugboard的可能   20%
###  1051433葛東昇 轉盤輪轉debug 利用接電板組合去編寫一份first_letter.py但答案與正解不一樣  20%
###  1051518李政憲 找出我們這組固定轉盤的 PLUGBOARD,找出最後答案  40%
###  1051434蔡適謙 開GIT 初始code  20%
