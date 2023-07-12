<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Source>
 */
class SourceFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        $source = $this->faker->randomElement(['krebs', 'thn', 'cisa', 'secweek']);

        return [

            'title' => $this->faker->company(),
            'content' => $this->faker->text(),
            'type' => $source,
            'logo' => $this->selectLogo($source)
        ];
    }

    protected function selectLogo($source){
        if($source === 'krebs'){
            return 3;
        } elseif($source === 'thn'){
            return 2;
        } elseif($source === 'cisa'){
            return 4;
        } else{
            return 1;
        }
    } 

}
