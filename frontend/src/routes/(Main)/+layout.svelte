<script>
    import { page } from '$app/stores';

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

    function updateRouteInfo(selectedRoute, routeName){
        currentRoute = selectedRoute;
        pageTitle = routeName
    }

</script>

<main class="MainRoutesContainer">
    <div class="MainRouteHeader">
        <img class="MainRouteHeader__logo" src="logo.png" alt="">
        <span class="MainRouteHeader__route">{pageTitle}</span>
    </div>
    <slot />

    <nav class="MainRouteNavbar">
        <div class="NavbarRoutes">

            {#each routes as route}
                <a on:click={() => {updateRouteInfo(route.route, route.title)}}
                    href="{route.route}" 
                    class="NavbarRoute
                    {route.route === currentRoute && 'selected'}"
                >
                    <i class="fa-solid {route.icon}"></i>
                
                </a>
            {/each}

            <a href="/news" class="NavbarRoute">
                <i class="fa-solid fa-home"></i>
            </a>

        </div>
    </nav>

</main>


<style lang="scss">
    .MainRoutesContainer{
        display: grid;
        display: -ms-grid;
        display: -moz-grid;
        padding: 0;
        margin: 0;
        width: 100vw;
        height: 100vh;
        position: absolute;
        grid-template-columns: repeat(20, 1fr);
        grid-template-rows: repeat(20, 1fr);

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
                width: 4rem;
                height: 4rem;
            }

            .MainRouteHeader__route{
                @include gradientText;
                font-size: 2.5rem;
                font-family: $primaryFont;
                margin-left: 1rem;
                letter-spacing: .2rem;
            }
        
        }

        .MainRouteNavbar{
            grid-column: 2/20;
            grid-row: 17/20;
            height: 100%;
            width:100%;
            display: flex;
            display: -ms-flexbox;
            display: -webkit-flex;
            justify-content: center;
            color: white;

            .NavbarRoutes{
                display: flex;
                display: -ms-flexbox;
                display: -webkit-flex;
                flex-direction: row;
                font-size: 2.3rem;
                text-decoration: none;

                .NavbarRoute{
                    margin-left: 1rem;
                    margin-right: 1rem;
                    color: white;

                }

                .selected{
                    @include gradientText;
                }

            }
        }
    }
</style>