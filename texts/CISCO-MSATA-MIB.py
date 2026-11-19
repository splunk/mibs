#
# PySNMP MIB module CISCO-MSATA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MSATA-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMsataMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 860))
ciscoMsataMIB.setRevisions(('2019-01-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMsataMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMsataMIB.setLastUpdated('201901090000Z')
if mibBuilder.loadTexts: ciscoMsataMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMsataMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ir800@cisco.com')
if mibBuilder.loadTexts: ciscoMsataMIB.setDescription('As part of this enhancement, adding SNMP support for below 2\n        mSata parameters on the IR829M products:\n        1) Lifetime remaining (wear leveling)\n        2) Memory usage for the mSATA SSD\n\n        This feature is supported in IR829M only.\n\n        *** ABBREVIATIONS, ACRONYMS, AND SYMBOLS ***\n\n        Wl      -   Wear Leveling of mSATA SSD')
ciscoMsataMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 860, 0))
ciscoMsata = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 860, 0, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMsata.setStatus('current')
if mibBuilder.loadTexts: ciscoMsata.setDescription('An entry containing the management information for a mSata\n        parameters - Lifetime remaining and memory usage.')
mibBuilder.exportSymbols("CISCO-MSATA-MIB", ciscoMsataMIBObjects=ciscoMsataMIBObjects, ciscoMsata=ciscoMsata, PYSNMP_MODULE_ID=ciscoMsataMIB, ciscoMsataMIB=ciscoMsataMIB)
