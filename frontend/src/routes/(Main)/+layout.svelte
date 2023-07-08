<script>
    import { page } from '$app/stores';
    import Navbar from "$lib/Main/Navbar/+page.svelte";
    import Header from "$lib/Main/Header/+page.svelte";

    const routes = [
        {route:'/news', icon:'fa-newspaper', title:'News'},
        {route:'/bookmarks', icon:'fa-bookmark', title:'Bookmarks'},
        {route:'/settings', icon:'fa-gear', title:'Settings'},
    ]
    
    let currentRoute = $page.url.pathname;

    let routeObj = routes.filter(route => {
        return route.route === currentRoute
    })
    let pageTitle = routeObj[0].title

    function updateRouteInfo(event){
        currentRoute = event.detail.route;
        pageTitle = event.detail.name;
    }

</script>

<main class="MainRoutesContainer">
    
    <Header pageTitle={pageTitle} />

    <div class="MainRouteContainer">
        <slot />
    </div>

    <Navbar currentRoute={currentRoute} on:route={updateRouteInfo} />

</main>


<style lang="scss">
    .MainRoutesContainer{
        display: grid;
        display: -ms-grid;
        display: -moz-grid;
        padding: 0;
        margin: 0;
        width: 100vw;
        height: 95vh;
        grid-template-columns: repeat(20, 1fr);
        grid-template-rows: repeat(20, 1fr);

        
        .MainRouteContainer{
            grid-column: 1/21;
            grid-row: 4/19;
        }

    }
</style>