import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

public final class SetOperations {
    public static void main(String[] args) throws IOException{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        Set<Integer> set1 = inputIntSet(reader);
        Set<Integer> set2 = inputIntSet(reader);
        prettyPrintSet("Set 1", set1);
        prettyPrintSet("Set 2", set2);

        Set<Integer> union = setUnion(set1, set2);
        prettyPrintSet("Set 1 union Set 2", union);

        Set<Integer> intersection = setIntersection(set1, set2);
        prettyPrintSet("Set 1 intersection Set 2", intersection);

        Set<Integer> difference = setDifference(set1, set2);
        prettyPrintSet("Set 1 difference Set 2", difference);

        difference = setDifference(set2, set1);
        prettyPrintSet("Set 2 difference Set 1", difference);

        Set<Integer> symmetricDifference = setSymmetricDifference(set1, set2);
        prettyPrintSet("Set 1 symmetric difference Set 2", symmetricDifference);
    }

    private static Set<Integer> setUnion(Set<Integer> set1, Set<Integer> set2) {
        Set<Integer> union = new HashSet<>(set1);
        union.addAll(set2);
        return union;
    }

    private static Set<Integer> setIntersection(Set<Integer> set1, Set<Integer> set2) {
        Set<Integer> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);
        return intersection;
    }

    private static Set<Integer> setDifference(Set<Integer> set1, Set<Integer> set2) {
        Set<Integer> difference = new HashSet<>(set1);
        difference.removeAll(set2);
        return difference;
    }

    private static Set<Integer> setSymmetricDifference(Set<Integer> set1, Set<Integer> set2) {
        Set<Integer> symmetricDifference = setUnion(set1, set2);
        symmetricDifference.removeAll(setIntersection(set1, set2));
        return symmetricDifference;
    }

    private static Set<Integer> inputIntSet(BufferedReader reader) throws IOException {
        return Arrays.stream(reader.readLine().split("\\s")).map(Integer::valueOf).collect(Collectors.toSet());
    }

    private static void prettyPrintSet(String msg, Set<Integer> set) {
        System.out.println(msg + " : " + set);
    }
}
