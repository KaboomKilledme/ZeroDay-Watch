{#if type}
    <div class="Exist Notify {type}">
        <p class="Notify__text">{text}</p>
    </div>
{/if}


<script>
    import { onMount } from "svelte";
    export let text;
    export let type;
    
    onMount(() => {
        setTimeout(() => {
            const Notification = document.querySelector('.Exist');
            if(Notification){
                Notification.remove();
            }

        },5000)
    })

</script>

<style lang="scss">

    .Exist{
        z-index: 10;
        margin-top:2rem;  
        text-align: center;
        height: 4rem;
        width: 100%;
        padding: 0;
        margin: 0;
        margin-top: auto;      
    }
    .showList{
        z-index: 10;
    }
    .Notify{
        display: flex;
        display: -ms-flexbox;
        display:-webkit-flex;
        align-items: center;
        font-size: 1.5rem;
        min-width: 10rem;
        height: 3rem;
        position: absolute;
        margin: auto;
        padding: .5rem;
        animation-name: removeNotification;
        animation-duration: 5s;

        .Notify__text{
            text-align: center;
            font-family: $secondaryFont;
        }

    }

    .error{
        text-align: center;
        background-color: orangered;
        color:white;

    }

    .success{
        text-align: center;
        background-color: rgb(0, 221, 0);
        color:black;

    }
</style>