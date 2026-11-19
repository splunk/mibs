#
# PySNMP MIB module CISCO-DMN-DSG-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-ROOT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, enterprises, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "enterprises", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSPVTG = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429))
ciscoSPVTG.setRevisions(('2010-08-30 11:00', '2009-11-26 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSPVTG.setRevisionsDescriptions(('V01.00.01 2010-08-30\n                    Updated for adherence to SNMPv2 format.', 'V01.00.00 2009-11-26\n                    Initial Version.',))
if mibBuilder.loadTexts: ciscoSPVTG.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoSPVTG.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSPVTG.setContactInfo('Cisco Systems, Inc.\n        Customer Service \n        Postal: 170 W Tasman Drive\n        San Jose, CA 95134\n        USA  \n        Tel: +1 800 553 NETS\n        \n        E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoSPVTG.setDescription('Cisco top level MIB.')
ciscoSat = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2))
ciscoDMN = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2))
ciscoDSGUtilities = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5))
ciscoDSGProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 6))
mibBuilder.exportSymbols("CISCO-DMN-DSG-ROOT-MIB", ciscoSat=ciscoSat, ciscoSPVTG=ciscoSPVTG, PYSNMP_MODULE_ID=ciscoSPVTG, ciscoDSGProducts=ciscoDSGProducts, ciscoDSGUtilities=ciscoDSGUtilities, ciscoDMN=ciscoDMN)
