<script>
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    function closeBtn(){

        dispatch('close', {
            id: null
        })
    }

</script>

<div class="DeleteAccountPromptBorder">
    <div class="DeleteAccountPrompt">
        <p class="DeleteAccountPrompt__text">
            Are you sure you want to delete this account permanently?
        </p>

        <div class="DeleteAccountPrompBtns">
            <button class="PromptBtn">
                <i class="accept fa-solid fa-check"></i>
            </button>

            <button class="PromptBtn" on:click={closeBtn}>
                <i class="decline fa-solid fa-xmark"></i>
            </button>
        </div>
    </div>
</div>


<style lang="scss">
    
    .DeleteAccountPromptBorder{
        opacity: 0;
        animation-name: fadeIn;
        animation-duration: .5s;
        opacity: 1;

        margin: auto;
        width: 18rem;
        min-height: 13rem;
        position: fixed;
        background: -webkit-linear-gradient(50deg, red, purple);
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        align-items: center;
        justify-content: center;
        padding: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
        border-radius: 1rem;
        
        @media screen and (max-width: 370px){
            width: 70%;        
        }

        .DeleteAccountPrompt{
            background: black;
            width: 95%;
            height: 90%;
            position:absolute;
            border-radius: 1rem;
            display: flex;
            display: -ms-flexbox;
            display: -webkit-flex;
            flex-direction: column;
            
            justify-content: center;
            align-items: center;
            
            
            .DeleteAccountPrompt__text{
                height: 50%;
                display: flex;
                display: -ms-flexbox;
                display: -webkit-flex;
                flex-direction: row;
                padding: 0 .2rem 0.2rem;
                justify-content: center;
                align-items: center;
                color: white;
                text-align: center;
                font-size: 1.5rem;
                font-family: $primaryFont;
            }

            .DeleteAccountPrompBtns{
                margin: auto;
                display: flex;
                display: -ms-flexbox;
                display: -webkit-flex;
                flex-direction: row;
                justify-content: space-between;
                width: 30%;
                                
                .PromptBtn{
                    background:none;
                    border: none;
                    font-size: 2rem;
                                
                    .accept{
                        color: rgb(24, 231, 24);
                        &:hover{
                            color: white;
                        }
                    }

                    .decline{
                        color: red;
                        &:hover{
                            color: white;
                        }
                    }
                }
          
            }
        }
    }

</style>