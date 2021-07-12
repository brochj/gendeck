from inspect import cleandoc
import genanki

my_model = genanki.Model(
    1962161376,
    "Cloze wordlist",
    fields=[
        {"name": "Example Id"},
        {"name": "Word"},
        {"name": "CEFR"},
        {"name": "Speaking"},
        {"name": "Writing"},
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
            "qfmt": cleandoc(
                """
                {{cloze::Example}}
                <br/>
                <br/>
                {{Definition}}
                <br/>
                <br/>
                {{Image}}
                """
            ),
            "afmt": cleandoc(
                """
                <example_labels>{{Example Labels}}</example_labels>{{cloze::Example}}
                <br/>
                <example_context>{{Example Context}}</example_context>
                <br/><br/>

                {{Image}}
                <hr id="answer">
                <word>{{Word}}</word> <sub><word_type>{{Word Type}}</word_type></sub>
                <br/>
                <b>{{IPA NAm}}</b>
                <br/><br/>
                <def_level>{{Definition CEFR}}</def_level><def_context>{{Definition Context}}</def_context> {{Definition}}
                <br/>

                <grammar>{{Definition Grammar}} </grammar>
                <def_type>{{Definition Type}} </def_type>
                <labels>{{Definition Labels}} </labels>
                <br/>
                <labels>{{Definition Variants}} </labels>
                <use>{{Definition Use}} </use>  
                <br/>
                <p class="text-level"><b>Oxford Level:</b> <level>{{CEFR}}</level></p>
                <p class="text-level">Speaking: <wordgroup>{{Speaking}}</wordgroup> |
                Writing: <wordgroup>{{Writing}}</wordgroup></p>
                <br/>
                <hr/>
                <a href="{{Dict_link}}" class="oxfordButton">Oxford Dictionary</a>
                <a href="{{Longman_link}}" class="longmanButton">Longman Dictionary</a>
                <a href="{{Google_images}}" class="googleButton">Google Images</a>
                """
            ),
        },
    ],
    css=cleandoc(
        """
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
            font-size: 25px;
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
        wordgroup {
            font-weight: 700;
            color: #F1431E
        }
        .text-level {
            font-size: 18px
        }
        def_level{
            font-size: 17px;
            font-weight: 700;
            color: #6390ff;
        margin-right: 10px
        }
        grammar {
            font-size: 14px;
            font-weight: 500;
            color: #6f6f6f;
        }
        labels { 
            font-size: 17px;
            font-style: italic;
            font-weight: 500;
            color: #6f6f6f;
        }

        def_type {
            font-size: 17px;
            font-style: italic;
            font-weight: 500;
            color: #5f55f5;
        }
        def_context {
            font-size: 17px;
            font-weight: 700;
            color: #333;
            margin-right: 9px
        }
        use { 
            font-size: 17px;
            font-weight: 700;
            color: #df4556;
        }
        word_type {
            font-style: italic;
            font-size: 17px;
            margin-left: 5px;
            color: #777
        }
        example_labels {
            font-size: 15px;
            font-style: italic;
            font-weight: 500;
            color: #6f6f6f;
            margin-right: 10px;
        }
        example_context {
            font-size: 15px;
            font-style: italic;
            font-weight: 600;
            color: #df4556;
        }
        """
    ),
)
