<div class="MainPage">
    <main class="MainContainer">
        <slot />
    </main>
</div>


<style lang="scss">
    .MainPage{
        width: 100%;
        padding:0;
        margin:0;
        background: $backgroundColour
    }

    .MainContainer{
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;

        flex-direction: column;
        
        margin: auto;
        height: 100%;
    
    }
</style>