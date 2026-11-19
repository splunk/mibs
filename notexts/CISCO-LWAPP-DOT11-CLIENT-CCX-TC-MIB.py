#
# PySNMP MIB module CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappDot11ClientCCXTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 611))
ciscoLwappDot11ClientCCXTextualConventions.setRevisions(('2007-03-22 00:00', '2007-02-22 00:00', '2007-02-19 00:00', '2007-01-30 00:00',))
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setLastUpdated('200703220000Z')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setOrganization('Cisco Systems Inc.')
class CiscoLwappDot11ClientReqStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("initiate", 1), ("inProgress", 2), ("success", 3), ("failure", 4), ("requestNotProcessedByClient", 5))

class CiscoLwappDot11ClientSSId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CiscoLwappDot11ClientAuthMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 255))
    namedValues = NamedValues(("none", 0), ("preSharedKey", 1), ("eap", 2), ("unknown", 255))

class CiscoLwappDot11ClientEAPMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 255))
    namedValues = NamedValues(("leap", 0), ("eapFast", 1), ("eapTls", 2), ("eapTtls", 3), ("peap0EapMschap2", 4), ("peap1EapGtc", 5), ("eapMd5", 6), ("eapSim", 7), ("preSharedKey", 8), ("unknown", 255))

class CiscoLwappDot11ClientKeyMgmtMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 255))
    namedValues = NamedValues(("none", 0), ("staticWep", 1), ("dynamicWep", 2), ("wpa", 3), ("wpaCckm", 4), ("wpa2", 5), ("wpa2Cckm", 6), ("cckm", 7), ("unknown", 255))

class CiscoLwappDot11ClientEncryptionMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))
    namedValues = NamedValues(("none", 0), ("wep40", 1), ("wep104", 2), ("tkip", 3), ("ckip", 4), ("aesCcmp", 5), ("unknown", 255))

class CiscoLwappDot11ClientCredentialType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 255))
    namedValues = NamedValues(("localSaved", 0), ("manuallyPrompted", 1), ("hostOsLogin", 2), ("unknown", 255))

class CiscoLwappDot11ClientPowerSaveMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 255))
    namedValues = NamedValues(("awake", 0), ("normal", 1), ("maxPower", 2), ("uApsd", 3), ("sApsd", 4), ("unknown", 255))

class CiscoLwappDot11ClientTxPowerMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fixed", 0), ("automatic", 1))

class CiscoLwappDot11ClientRadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unused", 0), ("fhss", 1), ("dsss", 2), ("irBaseband", 3), ("oFdm", 4), ("highRateDsss", 5), ("erp", 6), ("draft11n2point4Ghz", 7), ("draft11n5Ghz", 8))

class CiscoLwappDot11ClientDataRates(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("mhz1", 0), ("mhz2", 1), ("mhz5point5", 2), ("mhz6", 3), ("mhz9", 4), ("mhz11", 5), ("mhz12", 6), ("mhz18", 7), ("mhz24", 8), ("mhz36", 9), ("mhz48", 10), ("mhz54", 11))

mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB", CiscoLwappDot11ClientAuthMethod=CiscoLwappDot11ClientAuthMethod, CiscoLwappDot11ClientRadioType=CiscoLwappDot11ClientRadioType, CiscoLwappDot11ClientDataRates=CiscoLwappDot11ClientDataRates, CiscoLwappDot11ClientReqStatus=CiscoLwappDot11ClientReqStatus, ciscoLwappDot11ClientCCXTextualConventions=ciscoLwappDot11ClientCCXTextualConventions, CiscoLwappDot11ClientSSId=CiscoLwappDot11ClientSSId, CiscoLwappDot11ClientCredentialType=CiscoLwappDot11ClientCredentialType, CiscoLwappDot11ClientKeyMgmtMethod=CiscoLwappDot11ClientKeyMgmtMethod, CiscoLwappDot11ClientPowerSaveMode=CiscoLwappDot11ClientPowerSaveMode, PYSNMP_MODULE_ID=ciscoLwappDot11ClientCCXTextualConventions, CiscoLwappDot11ClientEAPMethod=CiscoLwappDot11ClientEAPMethod, CiscoLwappDot11ClientEncryptionMethod=CiscoLwappDot11ClientEncryptionMethod, CiscoLwappDot11ClientTxPowerMode=CiscoLwappDot11ClientTxPowerMode)
