`timescale 1ns/1ps

/**
 * Vulnerable Comparator: Non-Constant-Time Comparison
 * 
 * Vulnerability: Early return on mismatch leaks secret bit position through timing
 * Execution time ∝ position of first differing bit
 */

module vulnerable_comparator #(
    parameter WIDTH = 32,
    parameter CYCLES_PER_BIT = 10
)(
    input clk,
    input reset,
    input [WIDTH-1:0] secret,
    input [WIDTH-1:0] guess,
    output reg match,
    output reg [15:0] execution_cycles
);

    always @(posedge clk) begin
        if (reset) begin
            match = 1'b0;
            execution_cycles = 16'd0;
        end else begin
            match = 1'b1;
            execution_cycles = 16'd0;
            
            // ⚠️ NON-CONSTANT-TIME COMPARISON - TIMING LEAK!
            // Early exit on mismatch reveals first differing bit position
            for (integer i = WIDTH-1; i >= 0; i = i - 1) begin
                execution_cycles = execution_cycles + CYCLES_PER_BIT;
                
                if (secret[i] != guess[i]) begin
                    match = 1'b0;
                    // Early return - execution time leaks vulnerability!
                    // Time reveals: (WIDTH - i - 1) * CYCLES_PER_BIT
                end
            end
        end
    end

endmodule

/**
 * Secure Comparator: Constant-Time Reference Implementation
 * 
 * No early exit - always compares all bits regardless of matches
 */
module secure_comparator #(
    parameter WIDTH = 32,
    parameter CYCLES_PER_BIT = 10
)(
    input clk,
    input reset,
    input [WIDTH-1:0] secret,
    input [WIDTH-1:0] guess,
    output reg match,
    output reg [15:0] execution_cycles
);

    always @(posedge clk) begin
        if (reset) begin
            match = 1'b0;
            execution_cycles = 16'd0;
        end else begin
            match = 1'b1;
            execution_cycles = 16'd0;
            
            // ✓ CONSTANT-TIME COMPARISON
            // Always processes all bits - timing independent of data
            for (integer i = WIDTH-1; i >= 0; i = i - 1) begin
                execution_cycles = execution_cycles + CYCLES_PER_BIT;
                
                // Continue checking all bits even after mismatch
                if (secret[i] != guess[i]) begin
                    match = 1'b0;
                end
            end
        end
    end

endmodule
