<script>
    import { createEventDispatcher } from "svelte";

    export let content;
    export let isBookmark = false;

    const dispatch = createEventDispatcher()

    function closeBtn(){
        dispatch('close', {
            source:{id:null}
        })
    }

    function removeSave(id){
        dispatch('saved', {
            id:id
        })
    }

</script>

<div class="ContentBorder">
    <div class="Content">
        <div class="ContentText">

            <p class="ContentText__title">
                {content.title}
            </p>

            <p class="ContentText__text">
                {content.content}
            </p>
        </div>
        
        <div class="ContentOptions">
            <button class="ContentOptions__btn closeBtn" on:click={closeBtn}>
                <i class="ContentIcon fa-solid fa-xmark"></i>
            </button>
            {#if !isBookmark}
            <button class="ContentOptions__btn ContentOptionsBtnEffect">
                <i class="ContentIcon fa-solid fa-bookmark"></i>
            </button>
            {:else if isBookmark}
                <button class="ContentOptions__btn ContentOptionsBtnEffect" on:click={() => [removeSave(content.id), closeBtn()]}>
                    <i class="ContentIcon fa-solid fa-trash"></i>
                </button>
            {/if}

        </div>
    </div>
</div>

<style lang="scss">

    .ContentBorder{
        position: fixed;
        height: 90%;
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        align-items: center;
        justify-content: center;
        width: 52rem;
        transition: 1s;
        margin:auto;
        margin-top: 2rem;
        justify-self: center;
        align-self: center;
        background:$linearGradient1;
        border-radius: 2rem;

        @media screen and (max-width:846px){
            width: 90%;
        }

        .Content{
            display: grid;
            display: -ms-grid;
            display: -moz-grid;
            padding: 0;
            margin: 0;
            grid-template-columns: repeat(20, 1fr);
            grid-template-rows: repeat(20, 1fr);
            height: 95%;
            width: 95%;
            border-radius: 1.5rem;
            background: $backgroundColour;

            .ContentText{
                grid-column: 1/21;
                grid-row: 1/18;
                overflow-y: scroll;
                width: 95%;
                height: 100%;
                margin: auto;
                margin-top: 1rem;

                .ContentText__title{
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                    font-size: 1.3rem;
                    background: $linearGradient1;
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }

                .ContentText__text{
                    color: white;
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                    width: 100%;
                    font-size: 1.2rem;
                }
            }

            .ContentOptions{
                grid-row: 18/21;
                grid-column: 10/20;
                padding: 0;
                margin-top: 1rem;
                display: flex;
                display: -ms-flexbox;
                display: -webkit-flex;
                flex-direction: row;
                align-items: center;
                justify-content: flex-end;

                .ContentOptions__btn{
                    border: none;
                    background:none;

                    .ContentIcon{
                        font-size: 2rem;
                        margin-left: 1.5rem;
                    }
                }

                .closeBtn{
                    color: orangered;
                    &:hover{
                        color: white;
                    }
                }

                .ContentOptionsBtnEffect{
                    color:white;
                    &:hover{
                        background: $linearGradient1;
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                    }
                }
            }
        }
    }
</style>