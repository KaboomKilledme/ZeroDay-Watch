<script>
     import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();

    export let currentRoute;

    function selectRoute(name, route){
        dispatch('route', {
            name:name,
            route:route
        })

    }

    const routes = [
        {route:'/news', icon:'fa-newspaper', title:'News'},
        {route:'/bookmarks', icon:'fa-bookmark', title:'Bookmarks'},
        {route:'/settings', icon:'fa-gear', title:'Settings'},
    ]

    

</script>


<nav class="MainRouteNavbar">
    <div class="NavbarRoutes">

        {#each routes as route}
            <a on:click={() => {selectRoute(route.title, route.route)}}
                href="{route.route}{route.route === '/news' ? '?krebs' : ''}" 
                class="NavbarRoute
                {route.route === currentRoute && 'selected'}"
            >
                <i class="fa-solid {route.icon}"></i>
            </a>
        {/each}

    </div>
</nav>

<style lang="scss">
    .MainRouteNavbar{
            grid-column: 2/20;
            grid-row: 19/21;
            height: 100%;
            width:100%;
            display: flex;
            display: -ms-flexbox;
            display: -webkit-flex;
            justify-content: center;
            align-items: center;
        
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
</style>