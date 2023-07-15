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
            'link' => 'link'
            
        ];
    }

}
