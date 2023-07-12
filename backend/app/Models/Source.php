<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Source extends Model
{
    use HasFactory;

    protected $fillable = [
        'title',
        'content',
        'type',
        'logo'
    ];

    public function users(){
        return $this->belongsToMany(User::class, 'source_users'); 
    }
    
}
