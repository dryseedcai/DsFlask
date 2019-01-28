class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            # python列表推导式
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book

    """
    服务器数据：
    {
      "books": [
        {
          "author": [
            "俞甲子",
            "石凡",
            "潘爱民"
          ],
          "binding": "平装16开",
          "category": "编程",
          "id": 197,
          "image": "https://img1.doubanio.com/lpic/s25136218.jpg",
          "images": {
            "large": "https://img1.doubanio.com/lpic/s25136218.jpg"
          },
          "isbn": "9787121085116",
          "pages": "459",
          "price": "65.00",
          "pubdate": "2009-4",
          "publisher": "电子工业出版社",
          "subtitle": "链接、装载与库",
          "summary": "这本书主要介绍系统软件的运行机制和原理，涉及在Windows和Linux两个系统平台上，一个应用程序在编译、链接和运行时刻所发生的各种事项，包括：代码指令是如何保存的，库文件如何与应用程序代码静态链接，应用程序如何被装载到内存中并开始运行，动态链接如何实现，C/C++运行库的工作原理，以及操作系统提供的系统服务是如何被调用的。每个技术专题都配备了大量图、表和代码实例，力求将复杂的机制以简洁的形式表达出来。本书最后还提供了一个小巧且跨平台的C/C++运行库MiniCRT，综合展示了与运行库相关的各种技术。\\n对装载、链接和库进行了深入浅出的剖析，并且辅以大量的例子和图表，可以作为计算机软件专业和其他相关专业大学本科高年级学生深入学习系统软件的参考书。同时，还可作为各行业从事软件开发的工程师、研究人员以及其他对系统软件实现机制和技术感兴趣者的自学教材。",
          "title": "程序员的自我修养",
          "translator": [

          ]
        },
        {
          "author": [
            "[美] Chad Fowler"
          ],
          "binding": "平装",
          "category": "编程",
          "id": 316,
          "image": "https://img1.doubanio.com/lpic/s6378707.jpg",
          "images": {
            "large": "https://img1.doubanio.com/lpic/s6378707.jpg"
          },
          "isbn": "9787115233523",
          "pages": "202",
          "price": "39.00元",
          "pubdate": "2010-8",
          "publisher": "人民邮电出版社",
          "subtitle": "程序员职业规划之道",
          "summary": "要在当今的IT职场取得成功，必须像经营企业那样对待你的事业。在本书中，你将学到如何规划自己的职业生涯，让它向着你选择的目标前进，使人生更快乐、更美好。\\n作者运用其独特的思维方式，启发程序员不能只注重技能上的提高，还要关注自己的职业发展。书中涉及新旧技术的取舍、技术与业务的关系、技术是要专精还是要广博等，相信这也是长久以来困扰你的问题。带着这些问题去阅读此书，定会受益良多。\\n此外，本书中的每一章都包含一篇或几篇各领域成功人士的文章，让你直接了解他们如何规划自己的职业生涯！",
          "title": "我编程，我快乐",
          "translator": [
            "于梦瑄"
          ]
        }
      ],
      "count": 15,
      "start": 0,
      "total": 1880
    }
    """
