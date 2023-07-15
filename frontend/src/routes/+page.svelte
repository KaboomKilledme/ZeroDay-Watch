<script>    
    import Header from "$lib/Home/Header/+page.svelte";
    import Intro from "$lib/Home/Intro/+page.svelte";
    import Guarantees from "$lib/Home/Guarantees/+page.svelte";
    import Sources from "$lib/Home/Sources/+page.svelte";
    import Team from "$lib/Home/Team/+page.svelte"
</script>


<section class="LandingPage">
    <Header />
    <Intro />
    <Guarantees />
    <Sources />
    <Team />
</section>

<style lang="scss">
    .LandingPage{
        height: 100%;
        
        @media screen and (min-width: 720px){
                width: 80%;
                margin: auto;
        }


        @media screen and (max-width: 480px){
            display: grid;
            display: -ms-grid;
            display: -moz-grid;
            grid-template-rows: 5rem 1.1fr .9fr;
            grid-template-columns: 1fr;
            margin-bottom: 1rem;
        }
    
    }
</style>