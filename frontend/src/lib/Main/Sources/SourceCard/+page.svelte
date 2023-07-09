<script>
    export let source;
    
    const isWhiteLogo = (source.type === "CISA" || source.type === 'SecWeek' ? true:false)
    const isKrebs = (source.type === "Krebs" ? true:false)

</script>

<div class="SourceBorder">
    <button class="Source">
        <div class="SourceLogoContainer">
            <div class="SourceLogo SourceLogo__pic CircleSourecLogo { isKrebs && "krebsSourceLogo"}">
                <img class="SourceLogo__pic
                { isWhiteLogo && 'whiteLogo'}
    
                { source.type === "THN" && 'thnLogo'} 
                circleLogo {isKrebs && "kerbsLogo"}"
                src="sources/source-{source.logo}-logo.png" alt="">
            </div>
        </div>

        <div class="SourceTitle">
            <p class="SourceTitle__text">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vel fuga laudantium, eos suscipit sit minima! Voluptatum neque laborum iste earum, assumenda necessitatibus numquam debitis aperiam amet excepturi quaerat dolorem reiciendis, itaque ea magni? Vel neque, blanditiis aut magni deleniti, ratione modi illo numquam voluptatum minus consequuntur incidunt quisquam excepturi totam nihil repellat, ea amet enim aliquam! Laudantium pariatur magnam excepturi, repudiandae obcaecati a facere quaerat voluptas odit illo! Ullam deserunt impedit ducimus. Ullam debitis cum libero quae quos vero tenetur doloribus fugiat consectetur facilis a tempore dolores, repellendus consequatur vitae blanditiis error. Quaerat placeat voluptatem numquam eos porro, cum unde.
            </p>
        </div>

    </button>
</div>


<style lang="scss">
    

.SourceBorder{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 90%;
    width: 15rem;
    padding: .3rem;
    border-radius: 1.5rem;
    background:$linearGradient1;
    margin: 0 .5rem 0 .5rem;
    margin: 1rem;
    
    .Source{
        width: 98%;
        height: 99%;
        background-color: rgb(26, 26, 26);
        border-radius: 1.5rem;
        
        display: grid;
        display: -ms-grid;
        display: -moz-grid;

        grid-template-columns: repeat(20, 1fr);
        grid-template-rows: repeat(20, 1fr);
        border: none;
        padding: 0;
        

        &:hover{
            opacity: 0;
        }

        .SourceLogoContainer{
            grid-row: 1/4;
            grid-column: 1/21;

            .SourceLogo{
                display: flex;
                align-items: flex-start;
                flex-direction: column;
                width:fit-content;
                height: 2rem;
                border-radius: 1.5rem;
                background:$linearGradient1;
                border-bottom-left-radius: 0;
                
            }

            .CircleSourecLogo{
                display: flex;

                align-items: center;
                justify-content: center;

                border-radius: 1.8rem;
                padding-left: 0;
                padding-right: 0.5rem;
                padding-bottom: 1.2rem;
                border-bottom-left-radius:0;
                border-top-right-radius: 0;
            }

            .krebsSourceLogo{
                padding-bottom:.7rem;
            }
    
        }


        .SourceTitle{
            grid-column: 2/20;
            grid-row: 3/18;
            padding: 0;
            display: flex;
            flex-direction: row;
            height: 100%;
            width: 100%;
            font-size: 1.5rem;
            color: white;
            margin-top: 1rem;

            .SourceTitle__text{
                height: 3.2rem;
                width: 100%;
                height: 100%;
                padding: 0;
                word-wrap: break-word;
                word-break: break-all;
                text-overflow: clip;
                background: $linearGradient1;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                text-overflow: clip;
                overflow-y: hidden;
            }

        }
        
    }

}

.SourceLogo__pic{
    height: 2rem;
    border-radius: 1.5rem;
    padding: .7rem;
    border-bottom-left-radius:0;
}

.circleLogo{
    border-top-right-radius: 0;
}

.whiteLogo{
    background-color: white;
}

.thnLogo{
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #28468e;
}

.kerbsLogo{
    padding: 0;
    height: 3rem;
    margin-top: -0.4rem;
}
</style>