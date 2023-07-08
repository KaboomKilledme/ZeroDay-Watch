<script>
    export let name;
    export let icon;
    export let isDelete = false;
</script>

<button class="OptionBorder {isDelete ? "DeleteAccountBorder":""}">
    <div class="Option {isDelete ? "DeleteAccount":""}">
        <span class="Option__title">
            <i class="icon fa-solid {icon}"></i>
            {name}
        </span>
    </div>
</button>


<style lang="scss">

.OptionBorder{
    border:none;
    display: flex;
    display: -ms-flexbox;
    display: -webkit-flex;
    align-items: center;
    justify-content: center;
    width: 17rem;
    height: 4rem;
    padding: .3rem;
    border-radius: 1.5rem;
    background:$linearGradient1;
    margin: .5rem 0 .5rem 0;

    .Option{

        padding: 0;
        margin:0;
        width: 99.8%;
        height: 99.8%;
        margin: .5rem 0 .5rem;
        border-radius: 1rem;
        background: rgb(31, 31, 31);

        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        align-items: center;
        justify-content: flex-start;
        flex-direction: row;
        color: white;  

        &:hover{
             background: $linearGradient1;
            color: black;
        }
        
        .Option__title{
            height: 100%;
            display: flex;
            display: -ms-flexbox;
            display: -webkit-flex;
            align-items: center;
            margin-left: 1rem;
            font-size: 1.2rem;
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            text-transform: uppercase;

            .icon{
                font-size: 1.5rem;
                margin-right: .5rem;
            }
        }

    }
}

.DeleteAccountBorder{
    background:-webkit-linear-gradient(50deg,red, purple);
    
    .DeleteAccount:hover{
        background:-webkit-linear-gradient(50deg,red, purple);
        color: white;

    }
}
</style>