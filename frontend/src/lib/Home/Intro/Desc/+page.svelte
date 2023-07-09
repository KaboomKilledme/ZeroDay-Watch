<div class="LandingPageDesc">
    <h1 class="LandingPageDesc__title">The Latest Cyber News</h1>

    <div class="LandingPageDesc__line"></div>

    <p class="LandingPageDesc__text">
        We provide the latest updates on threats to cyberspace, 
        to stay informed register now or log back in 
    </p>

    <div class="AuthRedirect">
        
        <a href="/register" class="AuthRedirect__btn">
            <span class="AuthRedirect__text">
                Register
            </span>
        </a>

        <a href="/login" class="AuthRedirect__btn">
            <span class="AuthRedirect__text">
                Login
            </span>
        </a>
    
    </div>
</div>


<style lang="scss">
    .LandingPageDesc{
        width: 100%;

        .LandingPageDesc__title{
            font-family: $primaryFont;
            background: $linearGradient1;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        
            color: $blue2;
            font-size: 1.5rem;
        }
        @media screen and (max-width:719px){
            margin-left: 1rem;
        }
        .LandingPageDesc__line{
            border: .1rem solid $blue2;
            width: 90%
        }

        .LandingPageDesc__text{
            color: white;
            font-family: $secondaryFont;
            width: 95%;
        
        }

        .AuthRedirect{
            margin-top: 2rem;

            .AuthRedirect__btn{
                display: inline-block;
                width: 7rem;
                height: 2rem;
                margin-top: .3rem;
                text-align: center;

                background:$linearGradient1;
                font-family: $primaryFont;
                text-decoration: none;
                color: black;
                text-transform: uppercase;
                letter-spacing: .1rem;

                &:hover{
                    background: rgb(43, 43, 43);
                    color: white;
                }

                .AuthRedirect__text{
                    font-size: .8rem;
                    height: 100%;
                    width: 100%;
                    display:flex;
                    display: -ms-flexbox;
                    display: -webkit-flex;
                    align-items: center;
                    justify-content: center;
                }
            }
        }
        
    }

</style>