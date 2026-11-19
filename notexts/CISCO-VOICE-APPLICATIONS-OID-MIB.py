#
# PySNMP MIB module CISCO-VOICE-APPLICATIONS-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-APPLICATIONS-OID-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceApplicationsOIDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 5))
ciscoVoiceApplicationsOIDMIB.setRevisions(('2004-06-17 00:00',))
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setLastUpdated('200406170000Z')
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setOrganization('Cisco Systems, Inc.')
cvaMIBOids = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1))
ciscoCallManager = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 1))
ciscoCallManagerExpress = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 2))
ciscoSRST = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 3))
ciscoBTS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 4))
ciscoCSPS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 5))
mibBuilder.exportSymbols("CISCO-VOICE-APPLICATIONS-OID-MIB", ciscoVoiceApplicationsOIDMIB=ciscoVoiceApplicationsOIDMIB, ciscoCSPS=ciscoCSPS, ciscoCallManager=ciscoCallManager, ciscoCallManagerExpress=ciscoCallManagerExpress, ciscoSRST=ciscoSRST, ciscoBTS=ciscoBTS, cvaMIBOids=cvaMIBOids, PYSNMP_MODULE_ID=ciscoVoiceApplicationsOIDMIB)
