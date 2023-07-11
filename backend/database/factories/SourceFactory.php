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

        return [

            'title' => $this->faker->company(),
            'content' => $this->faker->text(),
            'source' => $this->faker->randomElement(['Krebs', 'THN', 'CISA', 'SecWeek'])
        ];
    }

}
