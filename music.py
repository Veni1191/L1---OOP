class Music:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def details(self):
        print("The details are:")
        print(f"The name of the artist is {self.name}")
        print(f"The instrument {self.name} uses is {self.instrument}")


class SabrinaC(Music):
    def __init__(self, name, instrument, age, discovery):
        super().__init__(name, instrument)
        self.age = age
        self.discovery = discovery

    def info(self):
        print(f"Age:{self.age}")
        print(f"Discovery:{self.discovery}")
        print(
            "Sabrina Carpenter is known for her creativity, humour and innuendos in her songs. She is lively and confident, being a role model and icon to many. She is my favourite because she always is herself and never changes, she also is confident and caring. And her songs are catchy and upbeat, each sending a story passed the listener's ears every time."
        )


singer1 = SabrinaC(
    "Sabrina Carpenter",
    "Guitar and Piano",
    "26",
    "She was discovered through her 10 year hard work of making videos and content on youtube, catching the eyes of Disney directors and then she debuted in her first TV show making her acting and singing career from there.",
)
singer1.details()
singer1.info()


class TateM(Music):
    def __init__(self, name, instrument, age, discovery):
        super().__init__(name, instrument)
        self.age = age
        self.discovery = discovery

    def info(self):
        print(f"Age:{self.age}")
        print(f"Discovery:{self.discovery}")
        print(
            "Tate Mcrae is an excellent dancer and her vocals are unique. Being one of the youngest rising pop stars in the world, Tate Mcrae is known for her bass and electrifying music as well as her amazing dance skills showcasing in her concerts. Tate is very open which is what I like about her and is confident too."
        )


singer2 = TateM(
    "Tate Mcrae",
    "Piano",
    "22",
    "Tate Mcrae's career started when she was 9, dancing in 'So you think you can dance' as a finalist. She started to dance at worldwide shows like these and got fame. She started showing interest in singing, creating content on Youtube of her own songs, eventuyally growing a big online fanbase and signing her first label with RCA records.",
)

singer2.details()
singer2.info()