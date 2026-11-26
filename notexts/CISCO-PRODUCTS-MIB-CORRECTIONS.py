#
# PySNMP MIB module CISCO-PRODUCTS-MIB-CORRECTIONS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PRODUCTS-MIB-CORRECTIONS
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoModules, ciscoProducts = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules", "ciscoProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoProductsMIBCorrections = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 65535))
ciscoProductsMIBCorrections.setRevisions(('2014-11-27 00:00',))
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setLastUpdated('201411270000Z')
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setOrganization('The Netdisco project')
catalyst365024TS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1823))
catalyst365048TS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1824))
catalyst365024PS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1825))
catalyst365048PS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1826))
catalyst365024TD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1827))
catalyst365048TD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1828))
catalyst365024PD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1829))
catalyst365048PD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1830))
mibBuilder.exportSymbols("CISCO-PRODUCTS-MIB-CORRECTIONS", PYSNMP_MODULE_ID=ciscoProductsMIBCorrections, catalyst365024TD=catalyst365024TD, ciscoProductsMIBCorrections=ciscoProductsMIBCorrections, catalyst365024PD=catalyst365024PD, catalyst365048PD=catalyst365048PD, catalyst365024TS=catalyst365024TS, catalyst365048PS=catalyst365048PS, catalyst365048TS=catalyst365048TS, catalyst365024PS=catalyst365024PS, catalyst365048TD=catalyst365048TD)
