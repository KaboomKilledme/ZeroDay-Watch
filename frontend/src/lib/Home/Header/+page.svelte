<div class="LandingPageHeader">
    <div class="LandingPageHeaderContent">
        <img class="LandingPageHeaderContent__logo" src="logo.png" alt="">
        <span class="LandingPageHeaderContent__text">eroDay Watch</span>
    </div>
</div>

<style lang="scss">
    .LandingPageHeader{
        padding:0;
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        flex-direction: row;
        justify-content:flex-start;
        align-items: center;
        width: 100%;
        margin:auto;    
        background: $linearGradient1;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;

        @media screen and (max-width:719px){
            width:100%;
            display: flex;
            display: -ms-flexbox;
            display: -webkit-flex;
            flex-direction: column;
            align-items: center;
        }
        
        @media screen and (max-width: 408px) {
            font-size: 1.5rem;
        }

        .LandingPageHeaderContent{
            margin-top: 1rem;
            display:flex;
            display:-ms-flexbox;
            display: -webkit-flex;
            align-items: center;

            .LandingPageHeaderContent__logo{
                width: 3.5rem;
                height: 3.5rem;

                @media screen and (max-width: 408px) {
                    width:3rem;
                    height: 3rem;   
                }
            
            }

            .LandingPageHeaderContent__text{
                margin:0;
                margin-left:.2rem;
                font-family: $primaryFont;
            }
        }
    }
    
</style>