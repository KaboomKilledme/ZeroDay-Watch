
<div class="Sources">
    <h1 class="Sources__title">Our Sources</h1>

    <div class="OurSources">

        <a href="https://www.securityweek.com/" class="source source-1">
            <img class="source__logo source-1__logo"
             src="sources/source-secweek-logo.png" alt="">

            <span class="source__text"> Security Week</span>
        </a>
        
        <a href="https://thehackernews.com/" class="source source-2">
            <img class="source__logo source-2__logo " src="sources/source-thn-logo.png" alt="">
            <span class="source__text"> The Hacker News </span>
        </a >
        
        <a href="https://www.cisa.gov/" class="source source-3">
            <img class="source__logo source-3__logo" src="sources/source-cisa-logo.png" alt="">
            <span class="source__text"> Cybersecurity & Infrastructure Secuirty Agency</span>
        </a>

    </div>
    <a href="https://krebsonsecurity.com/" class="source-4">
        <img class="source-4__logo" src="sources/source-krebs-logo.png" alt="">
        <span class="source-4__text"> Krebs On Security</span>
    </a>
</div>


<style lang="scss">
    .Sources{
        width: 100%;
        display:flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        flex-direction: column;
        align-items: center;

        .Sources__title{
        
            background: $linearGradient1;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            color: white;
            font-family: 'Zekton';

            text-transform:uppercase;
            font-size: 2rem;
            letter-spacing: .2rem;
        }

        .OurSources{
            width: 20rem;
            display: grid;
            display: -ms-grid;
            display: -moz-grid;
            grid-template-columns: repeat(15, 1fr);
            grid-template-rows: repeat(3, 5rem);
            
            .source{
                display: flex;
                display: -ms-flexbox;
                display: -webkit-flex;
                flex-direction: row;
                width: 100%;
                height: 100%;
                align-items: center;
                color: white;
                border-radius: 1rem;
                text-decoration: none;
                

                &:hover{
                    background: $linearGradient1;

                    .source__logo{
                        animation: none;
                    }
                }
            }

            .source__logo{
                margin-left: 1.5rem;

                animation-name: glowing;
                animation-duration: 1s;
                animation-iteration-count: infinite;

            }
            .source__text{
                margin-left: .5rem;
                overflow-wrap: break-word;
                font-family: 'Zekton';
            }
            .source-1{
                grid-column: 2/15;
                grid-row: 1/2;

            }

            .source-1__logo{
                width: 3.5rem;
                background-color: white;
                border-radius: 50%;
            }

            .source-2{
                grid-column: 4/15;
                grid-row: 2/3;    
            }

            .source-2__logo{
                padding: 0;
                border-radius: 50%;
                border: solid .1rem #28468e;
                background-color: #28468e;
                width: 3.8rem;
            }

            .source-3{
                grid-column: 2/15;
                grid-row: 3/4;
                
            }

            .source-3__logo{
                width: 3.8rem;
                height: 3.8rem;
                border-radius: 50%;
                
            }

        }

    }

    .source-4{
        margin: auto;
        margin-top: 1rem;
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        flex-direction: column;
        margin-bottom: 2rem;
        padding: 1rem;
        border-radius: 1rem;
        &:hover{
            background: $linearGradient1;

            .source-4__logo{
                animation: none;
            }
        }
        }

        .source-4__logo{
            width: 12rem;
            border-radius: 1rem;
            margin-bottom: .5rem;
            animation: glowing 1s infinite;
        }


        .source-4__text{
            text-align: center;
            color: white;
            font-family: 'Zekton';
        }


    @keyframes glowing {
    0% {
      box-shadow: 0 0 .4rem $blue1;
    }
    50% {
      box-shadow: 0 0 1rem $blue1;
    }
    100% {
      box-shadow: 0 0 .4rem $blue1;
    }
}

</style>