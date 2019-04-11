/*
    Genesis - A toolkit for working with phylogenetic data.
    Copyright (C) 2014-2019 Lucas Czech and HITS gGmbH

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Contact:
    Lucas Czech <lucas.czech@h-its.org>
    Exelixis Lab, Heidelberg Institute for Theoretical Studies
    Schloss-Wolfsbrunnenweg 35, D-69118 Heidelberg, Germany
*/

#include "genesis/genesis.hpp"

#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace genesis;
using namespace genesis::placement;
using namespace genesis::tree;
using namespace genesis::utils;

// =================================================================================================
//     Main
// =================================================================================================

int main( int argc, char** argv )
{
    (void) argc;
    (void) argv;

    // Activate logging.
    utils::Logging::log_to_stdout();
    utils::Logging::details.date = true;
    utils::Logging::details.time = true;
    utils::Options::get().number_of_threads( 40 );
    LOG_BOLD << utils::Options::get().info();
    LOG_BOLD;

    std::string in_meta = "/home/lucas/Projects/data/bv/meta/meta_simple.csv";
    std::string out_svg = "/home/lucas/Dropbox/HITS/manuscripts/post-processing-methods/03_revision/svg/pf_bv_place_small_tw/nugent_squars.svg";

    LOG_INFO << "Reading data";
    auto dfr = MatrixReader<double>();
    dfr.csv_reader().separator_chars( "\t" );
    auto meta = dfr.read( from_file( in_meta ));
    LOG_INFO << "meta: " << meta.rows() << " x " << meta.cols();

    auto nugent = std::vector<double>( meta.rows() );
    for( size_t r = 0; r < meta.rows(); ++r ) {
        nugent[r] = meta(r,2);
    }

    std::sort( nugent.begin(), nugent.end() );
    auto map = ColorMap({ Color(0,0,1), Color(1,0,0) });
    auto colors = Matrix<Color>( 1, nugent.size() );
    for( size_t i = 0; i < nugent.size(); ++i ) {
        colors( 0, i ) = map( nugent[i] / 10.0 );
    }

    SvgDocument doc;
    doc << make_svg_matrix( colors );
    std::ostringstream out;
    doc.write( out );
    utils::file_write( out.str(), out_svg );

    LOG_INFO << "Finished";

    return 0;
}
