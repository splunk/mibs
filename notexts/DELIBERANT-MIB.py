#
# PySNMP MIB module DELIBERANT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/deliberant/DELIBERANT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:27 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Counter32, MibIdentifier, Integer32, IpAddress, NotificationType, ModuleIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Counter64, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "NotificationType", "ModuleIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Counter64", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
deliberant = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761))
deliberant.setRevisions(('2008-09-05 00:00',))
if mibBuilder.loadTexts: deliberant.setLastUpdated('200809050000Z')
if mibBuilder.loadTexts: deliberant.setOrganization('Deliberant')
dlbProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 1))
dlbAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 2))
dlbMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3))
dlbExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 7))
mibBuilder.exportSymbols("DELIBERANT-MIB", PYSNMP_MODULE_ID=deliberant, dlbAdmin=dlbAdmin, dlbExperimental=dlbExperimental, deliberant=deliberant, dlbMgmt=dlbMgmt, dlbProducts=dlbProducts)
