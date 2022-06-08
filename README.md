# dns_client

Assignment for developing a simple DNS client.

簡単なDNSクライアントを作成してください。

## 仕様

- `python3 dns_client.py DNSサーバ名 ドメイン名` として実行すると、DNSのAレコードを指定されたDNSサーバに問合せを行い、得られた応答を適切に表示する。
- DNSの仕様は、以下のページを参照。
  - [https://datatracker.ietf.org/doc/html/rfc1034](RFC 1034 Domain Names - Concepts and Facilities)
  - [https://datatracker.ietf.org/doc/html/rfc1035](RFC 1035 Domain Names - Implementation and Specification)
  - [https://jprs.co.jp/topics/2020/200515_2.html](JPRS - DNS関連RFCの日本語訳を公開（RFC 1034、RFC 1035、RFC 3901）)

## ヒント

- DNSのメッセージの一部の箇所ではビット単位で情報が詰め込まれている。RFCを読み取って仕様を確認するとともに、バイナリメッセージの作成、解読の技法を身につけよう。Pythonでは、[structモジュール](https://docs.python.org/ja/3/library/struct.html)でバイナリデータのパッキング、アンパッキングができる。バイト列のパッキングの際は、バイトオーダーに注意すること。ネットワークに送り出すデータ（2バイト以上のデータ。例えば16ビットの整数）はネットワークバイトオーダー（実際にはビッグエンディアン）に変換する必要があるし、ネットワークから届いたデータを、ローカルの2バイト以上のサイズのデータとして受け取るときには、ホストバイトオーダ（Intelマシンなら、リトルエンディアン）に変換しなければいけない。このあたりは、C言語向けに書いてあるネットワークプログラミングのテキストを参照のこと。
- バイト内にビット単位で情報を詰め込んだり、ビット単位のデータを読み取るにはビット操作に慣れる必要がある。ビット単位の論理演算、シフト等について確認しておこう。
- DNSでは、同じドメイン名を繰り返しメッセージに含めなくて良いように、ドメイン名の表現に工夫がされている。RFCを読み取って、正しくサーバからの応答をデコードできるようなコードを書こう。

### 動作例

```
prompt$ python3 dns_client.py 8.8.8.8 www.ishilab.net
# Hex dump
2d 01 81 80 00 01 00 02   00 00 00 00 03 77 77 77   -____________www
07 69 73 68 69 6c 61 62   03 6e 65 74 00 00 01 00   _ishilab_net____
01 c0 0c 00 05 00 01 00   00 0e 10 00 08 05 6b 75   ______________ku
6d 6f 33 c0 10 c0 2d 00   01 00 01 00 00 0e 10 00   mo3___-_________
04 99 7e d3 9f                                      _____


# Header
ID       11521
QR       1 Response
Opcode   0 QUERY
AA       0
TC       0
RD       1 Recursion Desired
RA       1 Recursion Available
Z        0
RCODE    0 No error
QDCOUNT  1
ANCOUNT  2
NSCOUNT  0
ARCOUNT  0

# Question
Question: www.ishilab.net A(1) IN(1)

# Answer
Resource:   www.ishilab.net
      Type: CNAME(5)
     Class: IN(1)
       TTL: 3600
  RDLENGTH: 8
     RDATA: kumo3.ishilab.net
Resource:   kumo3.ishilab.net
      Type: A(1)
     Class: IN(1)
       TTL: 3600
  RDLENGTH: 4
     RDATA: 153.126.211.159

# Authority

# Additional Information

prompt$
```
