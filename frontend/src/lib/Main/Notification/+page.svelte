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
    }
    .showList{
        z-index: 10;
        padding: 0;
        margin: 0;
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
        padding: .5rem 0 .5rem 0;
        animation-name: removeNotification;
        animation-duration: 5s;
       
        .Notify__text{
            text-align: center;
            font-family: $secondaryFont;
            margin-left: 1rem;
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