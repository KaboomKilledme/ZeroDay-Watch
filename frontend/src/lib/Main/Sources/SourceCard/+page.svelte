<script>
    import {createEventDispatcher} from "svelte";
    const dispatch = createEventDispatcher()

    function showContent(source){
        dispatch('showContent', {
            source:source
        })
    }

    export let source;

</script>

<div class="SourceBorder">
    <button class="Source" on:click={showContent(source)}>
        <div class="SourceLogoContainer">
            <div class="SourceLogo SourceLogo__pic CircleSourecLogo { source.type === "krebs" && "krebsSourceLogo"}">
                <img class="SourceLogo__pic
                { source.type === 'cisa' && 'whiteLogo'}
                { source.type === 'secweek' && 'whiteLogo'}

                { source.type === "thn" ? 'thnLogo':''} 
                circleLogo {source.type === "krebs" && "kerbsLogo"}"
                src="sources/source-{source.type}-logo.png">
            </div>
        </div>

        <div class="SourceTitle">
            <p class="SourceTitle__text">
                {source.title}
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
                height: 100%;
                width: 100%;
                font-size: 1.7rem;
                color: white;
                margin-top: 1rem;
                

                .SourceTitle__text{
                    word-wrap: break-word;
                    text-overflow: clip;
                    background: $linearGradient1;
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                    text-overflow: clip;
                    overflow-y: hidden;
                    overflow-x: hidden;

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