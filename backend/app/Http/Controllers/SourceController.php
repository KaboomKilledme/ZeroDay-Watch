<?php

namespace App\Http\Controllers;

use App\Models\Source;
use Illuminate\Http\Request;

class SourceController extends Controller
{
    public function getSources(Request $request){

        $type = $request->source;
        $sources = Source::where('type', $type)->get();
        return $sources;
    }
    
}