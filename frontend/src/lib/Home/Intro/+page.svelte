<script>
    import Desc from "$lib/Home/Intro/Desc/+page.svelte"
</script>

<div class="LandingPageIntro">
  
    <Desc />
</div>

<style lang="scss">
    .LandingPageIntro{
        margin: auto;
        width:100%;
    
        @media screen  and (max-width: 860px){
            display: flex;
            display: flexbox;
            display: -ms-flexbox;
            display: -webkit-flex;
            flex-direction: column;

        }

    
    }
</style>