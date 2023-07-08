<script>
    import Desc from "$lib/Home/Intro/Desc/+page.svelte"
</script>

<div class="LandingPageIntro">
    <div class="LandingPageImg">
        <img class="LandingPageImg__pic" src="/asset1.png" />
    </div>
    <Desc />
</div>

<style lang="scss">
    .LandingPageIntro{
        margin: auto;
        width:100%;
        margin-top: 2rem;


        @media screen and (min-width:720px) {
            display: grid;
            display: -ms-grid;
            display: -moz-grid;
            grid-template-columns: repeat(2, 1fr);
            grid-template-rows: repeat(1, 1fr) ;
        }
        @media screen  and (max-width: 860px){
            display: flex;
            display: flexbox;
            display: -ms-flexbox;
            display: -webkit-flex;
            flex-direction: column;

        }

    
        .LandingPageImg{
            grid-column: 2/3;
            width: 100%;
            padding: 0;
            margin: auto;
            margin-top: 0;
            display: flex;
            display: -webkit-flex;
            display: -ms-flexbox;

            @media screen  and (max-width:860px){
                justify-content: flex-end;
                align-items: flex-end;
            }

            .LandingPageImg__pic{
                width: 20rem;
                @media screen and (max-width: 720px){
                    width: 15rem;
        
                }
                @media screen and (max-width: 295px){
                    width: 12rem;
                }
            }
        }
    }
</style>