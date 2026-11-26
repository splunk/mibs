#
# PySNMP MIB module CISCO-PRODUCTS-MIB-CORRECTIONS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PRODUCTS-MIB-CORRECTIONS
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoProducts, ciscoModules = mibBuilder.importSymbols("CISCO-SMI", "ciscoProducts", "ciscoModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoProductsMIBCorrections = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 65535))
ciscoProductsMIBCorrections.setRevisions(('2014-11-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setRevisionsDescriptions(('\n            Initial version for the netdisco-mibs distribution.\n            Added OIDs for the Catalyst 3650 platform.\n        ',))
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setLastUpdated('201411270000Z')
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setOrganization('The Netdisco project')
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setContactInfo('\n        Mailing list: netdisco-users@lists.sourceforge.net\n        IRC: #netdisco on Freenode\n    ')
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setDescription('\n        This module augments the CISCO-PRODUCTS-MIB. It\n        defines additional object identifiers that are\n        assigned to various hardware platforms, and hence are\n        returned as values for sysObjectID.\n    ')
catalyst365024TS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1823))
catalyst365048TS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1824))
catalyst365024PS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1825))
catalyst365048PS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1826))
catalyst365024TD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1827))
catalyst365048TD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1828))
catalyst365024PD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1829))
catalyst365048PD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1830))
mibBuilder.exportSymbols("CISCO-PRODUCTS-MIB-CORRECTIONS", catalyst365024TD=catalyst365024TD, catalyst365048PS=catalyst365048PS, catalyst365024TS=catalyst365024TS, ciscoProductsMIBCorrections=ciscoProductsMIBCorrections, catalyst365048PD=catalyst365048PD, PYSNMP_MODULE_ID=ciscoProductsMIBCorrections, catalyst365048TD=catalyst365048TD, catalyst365024PD=catalyst365024PD, catalyst365048TS=catalyst365048TS, catalyst365024PS=catalyst365024PS)
