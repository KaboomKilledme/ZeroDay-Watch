<?php

namespace App\Http\Controllers;

use App\Models\Source;
use Illuminate\Http\Request;

class SourceController extends Controller
{
    public function getSources(Request $request){
        $source = $request->source;
        $sources = Source::where('source', $source)->get();
        return $sources;
    }

    
}