<script>
    let guarantees = [
        {id:1, title:'Trustworthy', icon:'fa-check', selected:false,
        text: "Our sources are well versed and deep within the industry promising expert insights and critics. With us, you can trust that you're receiving reliable insights and analysis to make informed decisions and protect yourself against cyber threats."

        },
        
        {id:2, title:'Vigilant', icon:'fa-eye', selected:true,
        text: "Our news feed keeps you one step ahead by providing real-time updates on the latest cyber threats, vulnerabilities, and attack vectors. Our dedicated team of experts monitors the ever-changing threat landscape, ensuring that you stay informed and prepared."

        },
        
        {id:3, title:'Responsive', icon:'fa-bolt', selected: false, 
            text:"Cybersecurity incidents can occur at any moment, demanding swift action and response. Our news feed is designed to be responsive to your needs, delivering real-time updates on breaking cybersecurity news. From major security breaches to critical vulnerabilities, we promptly cover and provide insights into the latest incidents."
        }
        ]
    
    let text = guarantees[1].text;
    let selected = 2;
    function selectGuarantee(id){
        guarantees.map(guarantee => guarantee.id === id && [
            text = guarantee.text,
            selected = guarantee.id
        ])
    }
</script>


<div class="Guarantees">
    <h1 class="Guarantees__title">
        Our Guarantees
    </h1>

    <div class="OurGuarantees">

        {#each guarantees as guarantee}
            <button class="OurGuaranteesIcon" on:click={() => selectGuarantee(guarantee.id)}>
                <i class="fa-solid {guarantee.icon} {guarantee.id === selected ? 'selected':''}"></i>
                <span class="OurGuaranteeIcon__title">{guarantee.title}</span>
                {#if guarantee.id === selected}
                    <div class="underline"></div>
                {/if}
            </button>
        {/each}

    </div>

    <p class="Guarantees__text"> {text}</p>
</div>


<style lang="scss">
    .Guarantees{
        width:100%;
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        flex-direction: column;
        align-items: center;

        .Guarantees__title{
            background: $linearGradient1;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2rem;
            font-family: $primaryFont;
        }

        .Guarantees__text{
            text-align: center;
            color: white;
            font-family: $secondaryFont;
        }

        .OurGuarantees{
            display: flex;
            display: -ms-flexbox;
            display: -webkit-flex;
            flex-direction: row;
            width: 100%;
            justify-content: space-evenly;
        

            .OurGuaranteesIcon{
            
                color:$blue3;
                font-size: 2.2rem;
                background:none;
                border: none;

                .OurGuaranteeIcon__title{
                    font-size: 1rem;
                    font-family: $secondaryFont;
                    color:white;
                }

                .underline{
                    margin-top: .5rem;
                    width:100%;
                    border: solid $blue2 .1rem;
                }

                .selected{
                    color:$blue2;
                }

            }

        }

    }
</style>