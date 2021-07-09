import genanki

MODEL = genanki.Model(
    1962161376,
    "Cloze wordlist",
    fields=[
        {"name": "CEFR"},
        {"name": "Speaking"},
        {"name": "Writing"},
        {"name": "Word"},
        {"name": "Word Type"},
        {"name": "IPA NAm"},
        {"name": "IPA Br"},
        #
        {"name": "Definition"},
        {"name": "Definition CEFR"},
        {"name": "Definition Grammar"},
        {"name": "Definition Type"},
        {"name": "Definition Context"},
        {"name": "Definition Labels"},
        {"name": "Definition Variants"},
        {"name": "Definition Use"},
        {"name": "Definition Synonyms"},
        #
        {"name": "Example"},
        {"name": "Example Context"},
        {"name": "Example Labels"},
        #
        {"name": "Google_images"},
        {"name": "Dict_link"},
        {"name": "Longman_link"},
        {"name": "Image"},
        {"name": "Tags"},
    ],
    templates=[
        {
            "name": "Card",
            "qfmt": "{{cloze::Example}}<br/><br/><b>Def:</b> {{Definition}}<br/><br/>{{Image}}",
            "afmt": '{{cloze::Example}}<br/><br/><b>Def:</b> {{Definition}}<br/><br/>{{Image}}<hr id="answer"><word>{{Word}}</word> <sub><i>{{Word Type}}</i></sub><br/><b>{{IPA NAm}}</b><br/><br/>Oxford Level: <level>{{English Level}}</level><br/>Longman Group: <wordgroup>{{Word Group}}</wordgroup><br/><br/><a href="{{Dict_link}}" class="oxfordButton">Oxford Dictionary</a><a href="{{Longman_link}}" class="longmanButton">Longman Dictionary</a><a href="{{Google_images}}" class="googleButton">Google Images</a>',
        },
    ],
    css="""
.card{
font-family: arial;
font-size: 20px;
text-align: center;
color: #000;
background-color: #fff
}
.cloze{
    font-weight: 700;
    color: #00f
}
word{
    font-weight: 700;
    color: #00f
}
level{
    font-weight: 700;
    color: #1e90ff
}
.oxfordButton{
    background: linear-gradient(to bottom, #3d94f6 5%, #1e62d0 100%);
    background-color: #3d94f6;
    border-radius: 6px;
    border: 1px solid #094793;
    display: inline-block;
    cursor: pointer;
    color: #fff;
    font-family: Arial;
    font-size: 15px;
    font-weight: 700;
    padding: 6px 24px;
    text-decoration: none;
    margin:10px
}
.oxfordButton:hover{
    background: linear-gradient(to bottom, #1e62d0 5%, #3d94f6 100%);
    background-color: #1e62d0
}
.oxfordButton:active{
    position: relative;
    top: 1px
}
.longmanButton{
    background:linear-gradient(to bottom, #3d94f6 5%, #314089 100%);
    background-color:#3d94f6;
    border-radius:6px;
    border: 1px solid #094793;
    display:inline-block;
    cursor:pointer;
    color:#ffffff;
    font-family:Arial;
    font-size:15px;
    font-weight:bold;
    padding:6px 24px;
    text-decoration:none;
    margin:10px
}
.longmanButton:hover{
    background:linear-gradient(to bottom, #314089 5%, #3d94f6 100%);
    background-color:#314089
}
.longmanButton:active{
    position:relative;
    top:1px
}
.googleButton{
    background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%);
    background-color:#f9f9f9;
    border-radius:6px;
    border:1px solid #dcdcdc;
    display:inline-block;
    cursor:pointer;
    color:#666666;
    font-family:Arial;
    font-size:15px;
    font-weight:bold;
    padding:6px 24px;
    text-decoration:none;
    margin:10px
}
.googleButton:hover{
    background:linear-gradient(to bottom, #e9e9e9 5%, #f9f9f9 100%);
    background-color:#e9e9e9
}
.googleButton:active{
    position:relative;
    top:1px
}
img{
    max-width:400px;
    height:auto;
    border-radius: 20px
}
wordgroup{
    font-weight: 700;
    color: #F1431E
}
  
""",
)
