<script>
    const roles = [
        {title:"UI Designer - David Gosoe", icon:"fa-pen"},
        {title:"Frontend Developer - David Gosoe", icon:"fa-laptop-code"},
        {title:"Backend Developer - David Gosoe", icon:"fa-gear"},
        {title:"Philanthropic Investor - Shariear Rahman", icon:"fa-hand-holding-dollar"},
    ]
    
</script>


<div class="Team">
    <span class="Team__title">Our Team</span>
    <div class="Roles">

        {#each roles as role}
            <div class="Role">
                <i class="Role__icon fa-solid {role.icon}"></i>
                <span class="Role__text">
                    {role.title}
                </span>
            </div>
        {/each}

    </div>
</div> 



<style lang="scss">
    
.Team{
    display: flex;
    display: -ms-flexbox;
    display: -webkit-flex;
    flex-direction: column;
    font-family: 'Zekton';
    color: white;
    text-align: center;
    align-items: center;

    
    .Team__title{
        font-size: 2rem;
        background: $linearGradient1;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    
    .Roles{
        width: 70%;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;

        .Role{
            width: 18rem;
            height: 4rem;
            margin: 1rem;
            display: flex;
            display: -ms-flexbox;
            display: -webkit-flex;
            display: -webkit-flex;
            flex-direction: row;
            background: $linearGradient1;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;


            .Role__icon{
                font-size: 2.5rem;
                background: -webkit-linear-gradient(#eee, #333);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            .Role__text{
                width: 80%;
                text-align: center;
                font-size: 1.1rem;
                margin-left: .5rem;

            
            }
        }

    }

}

</style>