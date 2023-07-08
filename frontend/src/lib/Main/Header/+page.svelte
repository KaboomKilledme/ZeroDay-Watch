<script>
    export let pageTitle
</script>

<div class="MainRouteHeader">
    <img class="MainRouteHeader__logo" src="logo.png" alt="">
    <span class="MainRouteHeader__route">{pageTitle}</span>
</div>


<style lang="scss">
    
    .MainRouteHeader{
        grid-column: 2/20;
        grid-row: 2/4;
        height: 100%;
        width:100%;
        display: flex;
        display: -ms-flexbox;
        display:-webkit-flex;
        flex-direction: row;
        align-items: center;

        .MainRouteHeader__logo{
            width: 3rem;
            height: 3rem;
        }

        .MainRouteHeader__route{
            @include gradientText;
            font-size: 2rem;
            font-family: $primaryFont;
            margin-left: .5rem;
            letter-spacing: .2rem;
        }
        
    }
</style>